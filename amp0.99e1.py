#! /usr/bin/env python

#################################################################################
#    amp.py v0.99                                                               #
#                                                                               #
#    Copyright Jeremy M. Brown, 2010-2012                                       #
#    jeremymbrown@gmail.com                                                     #
#                                                                               #
#  This program is free software; you can redistribute it and/or modify         #
#  it under the terms of the GNU General Public License as published by         #            
#  the Free Software Foundation; either version 3 of the License, or            #
#  (at your option) any later version.                                          #
#                                                                               #
#  This program is distributed in the hope that it will be useful,              #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of               #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                #
#  GNU General Public License for more details.                                 #
#                                                                               #
#  You should have received a copy of the GNU General Public License along      #
#  with this program. If not, see <http://www.gnu.org/licenses/>.               #
#                                                                               #
#################################################################################

VERSION = '0.99e1'

# Subversion changes for 0.99e1:
#    - edited entropy_test function. #entropy = entropy + math.log(float(ntopologies)) 
#
# Subversion changes for 0.99e:
#    - Can now obtain burnin from post-hoc MrConverge analysis
#
# Version changes since 0.98:
#    - Implemented multiprocessing using worker + queue system
#    - Sped up RF distance calculations by automatically filling distances for duplicate topologies
#      and removing duplicate calculations from entropy function
#    - Switched from getopt to argparse module for command line arguments
#    - Made internal changes to conform to PEP8 Python Style Guide
#
# Version changes since 0.97:
#    - Now pre-calculates the ordered vector of RF distances between trees whenever quantile
#      or IQR tests will be performed.  Can also provide multiple quantile values on a single
#      command line to avoid having to rerun AMP for different positions.
#    - Now implementing a variance in tree length statistic.
#
# Version changes since 0.96:
#    - Implements Bayes factor test statistic for reading output of steppingstone sampling from 
#      MrBayes 3.2.1. Expects two kinds of runs in a folder: some that positively constrain each 
#      branch in a set of branches and some that negatively constrain each branch in that set.
#
# Version changes since 0.95:
#    - Implements Bayes factor test statistic for reading output of model-switch thermodynamic
#      integration program written by me
#
# Version changes since 0.94:
#    - Corrects bug in 0.91-0.93 that failed to order the vector of RF distances when calculating
#      interquartile-based test statistics
#
# Version changes since 0.93:
#    - Corrects bug in 0.91-0.92 that failed to order the vector of RF distances when calculating
#      quantile-based test statistics.
#
# Version changes since 0.92:
#    - Corrects the implementation of the branch-specific likelihood ratio test statistic to
#      calculate the likelihood ratio between a positively constrained search and a negatively
#      constrained search for each branch, rather than between an unconstrained search and a
#      negatively constrained search
#
# Version changes since 0.91:
#    - Implements branch-specific likelihood ratio test statistic
#

"""
Program for the calculation of phylogenetic model adequacy test statistics based on analyses of
posterior predictive datasets.


NOTE: Requires the previous installation of Dendropy v3
"""

import math
import traceback
import argparse
import sys
import dendropy
from dendropy import treecalc
import signal
import time
import multiprocessing




def main():

    # Sends Ctrl-C interrupt signal to sigint_handler method
    signal.signal(signal.SIGINT, sigint_handler)
    
    print """
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                 #
#   AMP: Assessing Model adequacy with Predictive distributions   #
#                                                                 #
#                             v0.99                               #
#                                                                 #
#                        Jeremy M. Brown                          #
#                     jeremymbrown@gmail.com                      #
#                                                                 #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    """
    
    args = parse_input(sys.argv)
    
    NPROCS = multiprocessing.cpu_count()
    
    # If nworkers is not specified, use all available processors
    if args.nworkers == 0:
        args.nworkers = NPROCS
        
    print """{NPROCS} processors detected. Using {NWORKERS} workers...
    """.format(NPROCS = NPROCS, NWORKERS = args.nworkers)
    
    """
    # QUARTET  --  NEVER FULLY IMPLEMENTED
    # Calculates taxon_sets for three bipartitions (based on quartets in empirical greedy consensus 
    #    tree) for use in calculating the partition-specific entropy statistic
    if len(args.part_list) > 0:
    
        # Reads in empirical tree list
        emp_tree_list = read_emp_trees(args.basename,  # basename
                                   int(args.nruns), # number of replicate analyses
                                   args.burnin  # manual burn-in (default = 0)
        
        # Calculates empirical greedy consensus tree
        empGreedyCon = emp_tree_list.consensus(min_freq=0)
        
        # Calculates appropriate taxon sets
        triBipart = getBiparts(empGreedyCon,    # Empirical greedy consensus tree
                                args.part_list))        # List of taxon names
    """
    
    # Read in, calculate, and store test values for each pp dataset
    # Uses a worker + queue model
        
    job_queue = multiprocessing.JoinableQueue()
    [job_queue.put(i) for i in range(1, args.ndatasets + 1)] # Add pp replicates to queue
    job_queue.put('emp') # Add empirical dataset to queue
    
    # Tell workers to stop when there are no more replicates
    for i in range(args.nworkers):
        job_queue.put('STOP')
        
    out_queue = multiprocessing.JoinableQueue()
    
    print "Replicates completed:",
    sys.stdout.flush()
    
    processes = []
    
    for i in range(args.nworkers):
        process = multiprocessing.Process(target = worker, args = (args, job_queue, out_queue))
        process.daemon = True
        processes.append(process)
        process.start()
    
    while not job_queue.empty():    # Wait for replicates to finish
        # Exit if a worker process encounters an error
        if not all([process.exitcode in [None, 0] for process in processes]):
            sys.exit(1)
        time.sleep(1)   # Check every second
            
    # Pull results from queue and sort by replicate
    # After sorting by replicate, empirical will be last item in each list
    # Pop list to acquire empirical value
    results = [out_queue.get() for i in range(args.ndatasets + 1)]
    results.sort(key = lambda result: result.i)
        
    # Extract statistics from Result objects
    pp_quantiles = [result.pp_quantiles for result in results]
    pp_entropies = [result.pp_entropies for result in results]
    pp_iqrs = [result.pp_iqr for result in results]
    pp_bpps = [result.pp_bpps for result in results]
    pp_tls = [result.pp_tls for result in results]
    pp_tlVars = [result.pp_tlVar for result in results]
    likeRatios = [result.likeRatios for result in results]
    allBFs = [result.bfs for result in results]
    allmbSSbfs = [result.mbSSbfs for result in results]
    read_time = sum([result.read_time for result in results])
    calc_time = sum([result.calc_time for result in results])

    if args.timeit:
        print """
        
        Time spent reading trees: %f s, %f proc-s
        Time spent calculating test statistics: %f s, %f proc-s""" % (read_time / args.nworkers, read_time, 
                                                                      calc_time / args.nworkers, calc_time)

    if args.debug:
        print """pp_entropies:
        """
        print pp_entropies

    print """
    Calculating P-values..."""
    
    if args.outfile is not None:
        logfile = open(args.outfile, 'w')
    else:
        logfile = None
    
    if args.quantile:
        emp_quantile = pp_quantiles.pop()
        for i in range(len(args.quant_focal_breaks)):
            p_value(args, emp_quantile[i],
                    [replicate[i] for replicate in pp_quantiles], # Extracts ith quantile from pp_quantiles
                    ("%s-th %s-quantile Test Statistic" % (str(args.quant_focal_breaks[i]), str(args.quant_bin_nos[i]))),
                    logfile)
    
    if args.entropy:  # Calculates (and outputs) appropriate p-values for statistical entropy test statistic
        emp_entropy = pp_entropies.pop()
        p_value(args, emp_entropy, pp_entropies, "Entropy-based Test Statistic", logfile)

    if args.iqr:  # Calculates (and outputs) specified p-values for interquartile range test statistic
        emp_iqr = pp_iqrs.pop()
        p_value(args, emp_iqr, pp_iqrs, "Interquartile Range Test Statistic", logfile)
    
    if len(args.part_list) > 0:
        emp_bpp = pp_bpps.pop()
        p_value(args, emp_bpp, pp_bpps, "Bipartition Frequency Test Statistic", logfile)
    
    if args.length:
        emp_tl = pp_tls.pop()
        p_value(args, emp_tl, pp_tls, "Mean Treelength Test Statistic", logfile)
    
    if args.tlVar:
        emp_tlVar = pp_tlVars.pop()
        p_value(args, emp_tlVar, pp_tlVars, "Treelength Variance Test Statistic", logfile)                
    
    if args.likeConstraints > 0:
        emp_LikeRatios = likeRatios.pop()
        for i in range(len(emp_LikeRatios)):
            p_value(args, emp_LikeRatios[i],
                     [j[i] for j in likeRatios],
                     "Bipartition-Specific Likelihood Ratio Constraint %d Test Statistic" % (i + 1),
                     logfile)
    
    if args.bfConstraints > 0:
        emp_bfs = allBFs.pop()
        for i in range(len(emp_bfs)):
            p_value(args, emp_bfs[i],
                    [j[i] for j in allBFs],
                    "Bipartition-Specific Bayes Factor Constraint %d Test Statistic" % (i + 1),
                    logfile)
    
    if args.mbSSbfConstraints > 0:
        emp_mbSSbfs = allmbSSbfs.pop()
        for i in range(len(emp_mbSSbfs)):
            p_value(args, emp_mbSSbfs[i], [j[i] for j in allmbSSbfs],
                    "Bipartition-Specific MrBayes Steppingstone Bayes Factor Constraint %d Test Statistic" % (i + 1),
                    logfile)
    
    if args.outfile is not None:
        logfile.close()

    print """
    Program execution complete.  Exiting...
    """

def worker(args, in_queue, out_queue):
    """Worker function acquires task from input queue, calculates pp stats, stores results in output queue"""
    while True:
        try:
            rep = in_queue.get()
        except Queue.Empty:
            sys.exit(1)
        if rep == 'STOP':
            sys.exit(0)
        else:
            result = pp_calc(args, rep)
            out_queue.put(result)
            in_queue.task_done()
            print str(rep),
            sys.stdout.flush()

def pp_calc(args, i):
    """
    Read input and calculate posterior predictive statistics for a single replicate dataset, i.
    """
    
    read_start = time.clock()
    
    if args.quantile or args.entropy or args.iqr or args.length or args.tlVar or len(args.part_list) > 0:
        # Read in posterior predictive tree distributions from file (excluding burn-in)
        pp_tree_list = read_trees(args, i)
        
    # Checks to see if bipartition-specific LR statistic has been selected
    if args.likeConstraints > 0:
        # Read in likelihood scores for unconstrained and any constrained analyses
        likeScores = read_likelihoods(args, i)
        
    # Checks to see if bipartition-specific model-switch TI BF statistic has been selected
    if args.bfConstraints > 0:
        # Read in Bayes factors for each replicate
        bfs = read_bfs(args, i)
    else:
        bfs = []
    
    # Checks to see if bipartition-specific MrBayes steppingstone BF statistic has been selected
    if args.mbSSbfConstraints > 0:
        # Read in marginal likelihoods from pos and neg log files and calculates the corresponding BF
        mbSSbfs = readmbSSbfs(args, i)
    else:
        mbSSbfs = []
        
    read_end = time.clock()
        
    calc_start = time.clock()
                              
    # Calculate ordered RF vector if either quantile-position or IQR stats selected
    if args.quantile or args.iqr or args.entropy:
        (pp_rf_dists, pp_topo_freqs) = calcAndSortTreeDists(args, pp_tree_list)
    
    # Calculate quantile-based test statistic
    if args.quantile:
        pp_quantiles = quantile_test(args, pp_rf_dists) # Passes vector of ordered RF distances    
    else:
        pp_quantiles = []    

    # Calculate entropy-based test statistic
    if args.entropy:
        pp_entropies = entropy_test(args, pp_tree_list, pp_topo_freqs)
            # pp_tree_list is a DataSet object with a single TreeList 
            #   for the relevant pp data set -- creates copy of this and passes to entropy_test()
    else:
        pp_entropies = []

    # Calculate interquartile range test statistic
    if args.iqr:
        pp_iqr = iqr_test(args, pp_rf_dists)
    else:
        pp_iqr = []

    # Calculate partition-specific entropy test statistic
    if len(args.part_list) > 0:
        pp_bpps = partition_test(args, pp_tree_list)
    else:
        pp_bpps = []
    
    # QUARTET
    #if len(args.part_list) > 0:
    #    pp_bpps.append(partition_test(pp_tree_list))    

    # Calculate mean treelength test statistic
    if args.length:
        pp_tls = treelength_test(args, pp_tree_list)
    else:
        pp_tls = []

    # Calculate treelength variance test statistic
    if args.tlVar:
        pp_tlVar = tlVar_test(args, pp_tree_list)
    else:
        pp_tlVar = []

    # Calculate partition-specific likelihood ratio test statistic
    likeRatios = []
    if args.likeConstraints > 0:
        for j in range(len(likeScores)): # Iterates through branches and stores LRs in tempLikeRatios
            if j % 2 == 0:    # Skips odd numbers (corresponding to neg constraints)
                ratio = likeScores[j] - likeScores[j + 1] # Calcs ln(LR) as ln(posConL)-ln(negConL)   
                if ratio < 0.001 and ratio > -0.001: # Rounds down to zero when two scores are very similar
                    ratio = 0
                likeRatios.append(ratio)
        
    calc_end = time.clock()
    
    read_time = read_end - read_start
    calc_time = calc_end - calc_start
    
    result = Result(i, pp_quantiles, pp_entropies, pp_iqr, pp_bpps, pp_tls, pp_tlVar, likeRatios, bfs, mbSSbfs, read_time, calc_time)
    
    return result
    
class Result(object):
    """Store results from one replicate in convenient object format"""
    def __init__(self, i, pp_quantiles, pp_entropies, pp_iqr, pp_bpps, pp_tls, pp_tlVar, likeRatios, bfs, mbSSbfs, read_time, calc_time):
        self.i = i
        self.pp_quantiles = pp_quantiles
        self.pp_entropies = pp_entropies
        self.pp_iqr = pp_iqr
        self.pp_bpps = pp_bpps
        self.pp_tls = pp_tls
        self.pp_tlVar = pp_tlVar
        self.likeRatios = likeRatios
        self.bfs = bfs
        self.mbSSbfs = mbSSbfs
        self.read_time = read_time
        self.calc_time = calc_time
    def __repr__(self):
        return repr((self.i, self.pp_quantiles, self.pp_entropies, self.pp_iqr, self.pp_bpps, 
                     self.pp_tls, self.pp_tlVar, self.likeRatios, self.bfs, self.mbSSbfs, self.read_time, self.calc_time))
        
def p_value(args, emp_stat, pp_stats, test_stat_name, logfile):
    """
    Calculates specified p-values
    """
    
    less_than_count = 0
    for i in pp_stats:
        if i <= emp_stat:
            less_than_count += 1
    lower_p = float(less_than_count) / float(len(pp_stats))
    if args.lower and args.debug:
        print "Lower One-tailed P-value: %f" % lower_p
            
    greater_than_count = 0
    for i in pp_stats:
        if i >= emp_stat:
            greater_than_count += 1
    upper_p = float(greater_than_count) / float(len(pp_stats))
    if args.upper and args.debug:
        print "Upper One-tailed P-value: %f" % upper_p
        
    two_p = min(2 * min(lower_p, upper_p), 1)
    if args.twotailed and args.debug:
        print "Two-tailed P-value: %f" % two_p
        
    if args.outfile is not None:
    
        logfile.write("****** %s ******\n" % test_stat_name)
        logfile.write('\n')
    
        if args.v:
            ## Outputs all posterior predictive test statistic values
            logfile.write("Posterior Predictive %ss:\n" % test_stat_name)
            logfile.write('\n')
            for i in pp_stats:
                logfile.write(str(i)+'\n')
                
            ## Outputs empirical test statistic value
            logfile.write('\n')
            logfile.write("Empirical %s:\n" % test_stat_name)
            logfile.write('\n')
            logfile.write(str(emp_stat)+'\n')
            
        ## Outputs appropriate p-values
        logfile.write('\n')
        logfile.write("P-values:\n")
        logfile.write('\n')
        if args.lower:
            logfile.write("Lower One-tailed P-value: %f\n" % lower_p)
        if args.upper:
            logfile.write("Upper One-tailed P-value: %f\n" % upper_p)
        if args.twotailed:
            logfile.write("Two-tailed P-value: %f\n" % two_p)
        logfile.write('\n')
    
def getMrCburn(args, i):
    """
    getMrCburn() retrieves appropriate burnins from MrConverge log files.
    Files should be named as basename_data#.log.
    """
    try:
        file = "%s_%s.log" % (args.basename, str(i))
        mrcin = open(file, 'r')
        burnin = 0
        burnin_crit_list = []
        for line in mrcin:
            if line.find("BURNIN set to") != -1:
                burnin = int(line.split()[3])
            elif line.find("MaxBppCI:") != -1:
                burnin_crit_list = [float(x) for x in line.split()[1:]]
                
    except:
        print "\nProblem getting burn-in value from file %s. Exiting..." % file
        if args.debug:
            traceback.print_exc()
        sys.exit(1)
        
    if any(crit > 0.1 for crit in burnin_crit_list):
        print '\nCheck convergence for {file}. MaxBppCI > 0.1.'.format(file = file)
        
    if args.debug:    
        print "MrC burn for file %s_%s.log: %d" % (basename, str(data_no), burnin)
        
    return burnin

def read_trees(args, i):
    """
    Reads in trees resulting from analyses of posterior predictive datasets.
    """
    
    # Instantiates tree list
    pp_trees = dendropy.TreeList()

    try:    
        if not args.manual:
            args.burnin = getMrCburn(args, i)
    except:
        file = "%s_%s.log" % (args.basename, str(i))
        print '''
        Problem getting burnin for {file}
        Exiting...'''.format(file = file)
        if args.debug:
            traceback.print_exc()
        sys.exit(1)
            
    try:
        for j in range(1, args.nruns + 1):    # Iterates over 1, ..., nruns
            filename = "%s_%s_r%d.t" % (args.basename, str(i), j)
            pp_trees.read_from_path(filename, 'nexus', tree_offset=args.burnin, as_unrooted=True)
    except:
        print '''
        Problem reading in trees for {file}
        Exiting...'''.format(file = filename)
        if args.debug:
            traceback.print_exc()
        sys.exit(1)
        
    ## Currently some error with the DataSet.unify_taxa() method [1.7.10]
    # pp_trees.unify_taxa()    # Just to make sure all trees share the same TaxonSet
    
    # Returns a dataset object containing separate treelists for each pp dataset
    return(pp_trees)
    
def read_likelihoods(args, i):
    """
    Reads in likelihoods for positively and negatively constrained searches for each dataset.  
    Returns a list containing all likelihood scores for each replicate dataset.
    
    Example for N constraints:
    [posCon1,negCon1,posCon2,negCon2,...,posConN,negConN]        
    """
    
    likelihoods = []
    
    try:
        for j in range(1, int(args.likeConstraints) + 1):
            
            # Storing positive constraint likelihoods
            likeIn = open("%s_%s_bp%d.pos.constraint.best.tre" % (args.basename, str(i), j))
            tempLine = likeIn.readline()
            while (tempLine.find("!GarliScore") == -1):
                tempLine = likeIn.readline()
            scoreList = tempLine.split("][")
            score = float(scoreList[1].split(" ")[1])
            likelihoods.append(score)    
            likeIn.close()
            
            # Storing negative constraint likelihoods
            likeIn = open("%s_%s_bp%d.neg.constraint.best.tre" % (args.basename, str(i), j))
            tempLine = likeIn.readline()
            while (tempLine.find("!GarliScore") == -1):
                tempLine = likeIn.readline()
            scoreList = tempLine.split("][")
            score = float(scoreList[1].split(" ")[1])
            likelihoods.append(score)                
            likeIn.close()
            
    except:
        print "Problem reading in likelihood scores.  Exiting...."
        if args.debug:
            traceback.print_exc()
        sys.exit(1)
    
    return likelihoods

def read_bfs(args, i):
    """
    Reads in Bayes factors (actually ln(BFs)) estimated from model-switch thermodynamic 
    integration between a model that positively constrains some branch and one that negatively
    constrains it.  List simply contains ln(BF) values for each constraint.
    
    Example for N constraints:
    [ln(BF)1,ln(BF)2,...,ln(BF)N]
    """
    bfs = []
    
    try:
        for j in range(1, int(args.likeConstraints) + 1):  
            
            bfIn = open("%s_%s_bp%d.bf.out" % (args.basename, str(i), j))
            tempLine = bfIn.readline()
            while (tempLine.find("Estimated ln(Bayes Factor)") == -1):
                tempLine = bfIn.readline()
            bfVal = float(tempLine.split(" ")[4])
            bfs.append(bfVal)
            bfIn.close()
            
    except:
        print "Problem reading in Bayes factors. Exiting..."
        if args.debug:
            traceback.print_exc()
        sys.exit(1)
    
    return bfs
    
def readmbSSbfs(args, i):

    mbSSbfs = []

    try:
        for j in range(1, int(args.likeConstraints) + 1):    # Iterates from 1 to numCon
            posIn = open("%s_%s.con%d.pos.log" % (args.basename, str(i), j))
            negIn = open("%s_%s.con%d.neg.log" % (args.basename, str(i), j))
            posTempLine = posIn.readline()
            negTempLine = negIn.readline()
            while (posTempLine.find("Mean:") == -1):
                posTempLine = posIn.readline()
            while (negTempLine.find("Mean:") == -1):
                negTempLine = negIn.readline()
            posLike = float(posTempLine.strip().split()[1])
            negLike = float(negTempLine.strip().split()[1])
            bfVal = float(posLike - negLike)
            mbSSbfs.append(bfVal)
            posIn.close()
            negIn.close()
    except:
        print "Problem reading in MrBayes marginal likelihood values for %s dataset. Exiting..." % str(data_no)
        if args.debug:
            traceback.print_exc()
        sys.exit(1)

    return mbSSbfs

"""
    # Quartet
def getBiparts(greedyConTree,taxa):
    """
    #Function to find three bipartitions based on quartets surrounding a given bipartition in the 
    #empirical greedy consensus tree
"""
    try:
        # Defines the target bitmask based on the user input lists of taxa
        searchMask = bit_mask(taxa,greedyConTree.leaf_nodes())
        
        # Defines bitmasks for each internal node in the tree
        for i in greedyConTree.internal_nodes():
            i.label = bit_mask(i.leaf_nodes(),greedyConTree.leaf_nodes())
        
        # Locates the node corresponding to the specified bipartition using bitmasks
        focalNode = greedyConTree.find_node_with_label(searchMask)
        
        # Reroots the tree at the focal node so that the leaf_nodes() function can be used to 
        #    define the taxon sets in each part of the quartet
        greedyConTree.reroot_at(focalNode)
        
        # Defines taxon sets based on the quartet surrounding the bipartition of interest
        taxSet1 = greedyConTree.seed_node.child_nodes()[0].leaf_nodes()
        taxSet2 = greedyConTree.seed_node.child_nodes()[1].leaf_nodes()
        taxSet3 = greedyConTree.seed_node.child_nodes()[2].child_nodes()[0].leaf_nodes()
        taxSet4 = greedyConTree.seed_node.child_nodes()[2].child_nodes()[1].leaf_nodes()
        
        # NEED TO DEFINE THREE DIFFERENT PARTITIONS BASED ON THESE TAXON SETS AND RETURN THEM
        
    except:
        print "Problem getting three bipartitions from empirical greedy consensus tree. Exiting..."
        if args.debug:
            traceback.print_exc()
        sys.exit(1)    
"""

###############  Begin Test Statistic Functions ###############
        
def calcAndSortTreeDists(args, tree_data):
    """
    A function to calculate RF distances from a set of trees and sort them.  This sorted
    vector will then be used when calculating quantile-based values or interquantile
    distances.
    """
    
    try:
        # Create initial variables, including vector to hold pairwise RF values
        rf_dists = []
        
        tree_list = list(reversed(range(len(tree_data))))
        total_trees = float(len(tree_list))
        
        topo_freqs = []
        symm_diff = treecalc.symmetric_difference

        # Calculate and store all pairwise RF values

        while len(tree_list) > 1:
            j = tree_list.pop()
            current_rfs = []
            duplicate_trees = []
            for k in tree_list:
                # Calculates RFs b/w first tree and all others
                rf_dist = symm_diff(tree_data[j], tree_data[k])
                current_rfs.append(rf_dist)
                if rf_dist == 0:
                    duplicate_trees.append(k)
            rf_dists.extend(current_rfs)
            topo_freqs.append((current_rfs.count(0) + 1)/total_trees)

            # Autofill values for duplicate topologies
            while len(duplicate_trees) > 0:
                current_rfs.remove(0)
                temp = duplicate_trees.pop()
                tree_list.remove(temp)
                rf_dists.extend(current_rfs)
        rf_dists.sort()

        return (rf_dists, topo_freqs)

    except:
        print '\nProblem calculating and ordering RF distances...'
        if args.debug:
            traceback.print_exc()
        sys.exit(1)

def quantile_test(args, rf_dists):
    """
    Calculates positions of a set of k-th p-quantiles in ordered vector of RF distances 
    from one posterior distribution.
    """
    
    try:
        k = args.quant_focal_breaks
        p = args.quant_bin_nos
        quantile = []
        for i in range(len(k)):
            # Iterate and find k-th p-quantiles
            #     See definition of k-th p-quantile position in my manuscript
            g = (len(rf_dists)*int(k[i])) % int(p[i])
            j = (len(rf_dists)*int(k[i])) / int(p[i])
            if g == 0:
                quantile.append((float(rf_dists[j])+float(rf_dists[j+1]))/2)
            else:
                quantile.append(float(rf_dists[j+1]))
        return quantile

    except:
        print "Problem calculating quantile-based test statistic..."
        if args.debug:
            traceback.print_exc()
        sys.exit(1)

def entropy_test(args, trees, topo_freqs):
    """
    Calculates entropy-based test statistic for one posterior predictive dataset.
    Calculates change in entropy from the prior to the posterior
    Assuming a uniform prior on topologies, change in entropy can be calculated as:
    T(X) = (sum across topologies i=1 to N: post_i * ln(post_i)) - ln(prior_i)
    """
    
    try:
        total_trees = len(trees)

        ######  Calculates entropy test statistic for the posterior predictive data sets  #####

        #    Calculates change in entropy from the prior to the posterior
        #    -- Assuming a uniform prior on topologies, change in entropy can be calculated as:
        #        T(X) = (sum across topologies i=1 to N: post_i * ln(post_i)) - ln(prior_i)
            
        entropy = 0
        for j in range(len(topo_freqs)):
            entropy += topo_freqs[j] * math.log(topo_freqs[j])
        
        ntaxa = len(trees.taxon_set)        
        if args.debug:
            print "# Taxa: %d" % ntaxa
                
        ntopologies = factorial(2 * ntaxa - 4, ntaxa - 2) / int((math.pow(2, ntaxa - 2)))
        if args.debug:
            print "# Topologies: %d" % ntopologies

       #entropy = entropy + math.log(float(ntopologies)) # Should we correct for finite posterior size?
        
        if args.debug:
            print """
            Entropy = %f
            """ % entropy
    
        return(entropy)
    
    except:
        print "Problem calculating entropy-based test statistic..."
        if args.debug:
            traceback.print_exc()
        sys.exit(1)

def iqr_test(args, rf_dists):
    """
    Calculates interquartile distance (1st to 3rd quartile) for one posterior distribution
    """
    try:
        # Find 1st quartile
        #     See definition of k-th p-quantile position in my manuscript
        g = (len(rf_dists) * 1) % 4
        j = (len(rf_dists) * 1) / 4
        if g == 0:
            first_quant = float(rf_dists[j] + rf_dists[j+1]) / 2
        else:
            first_quant = float(rf_dists[j+1])

        # Find 3rd quartile
        #     See definition of k-th p-quantile position in my manuscript
        g = (len(rf_dists) * 3) % 4
        j = (len(rf_dists) * 3) / 4
        if g == 0:
            third_quant = (float(rf_dists[j]) + float(rf_dists[j+1])) / 2
        else:
            third_quant = float(rf_dists[j+1])    
    
        iqr = third_quant - first_quant
        
        return iqr
        
    except:
        print """
    Problem calculating interquartile range test statistic...
        """
        if args.debug:
            traceback.print_exc()
        sys.exit(1)

def partition_test(args, tree_data):
    """
    Calculates entropy of posterior distribution with two categories: (i) trees with a split or
    (ii) trees without a split.
    """
    
    try:
        p = tree_data.frequency_of_split(labels=args.part_list)
        if p < 1 and p > 0:
            ent_stat = - (p * math.log(p) + (1 - p) * math.log((1 - p)))
        else:
            ent_stat = 0
        return ent_stat
    
    except:
        print """
    Problem calculating bipartition frequency test statistic...
        """
        if args.debug:
            traceback.print_exc()
        sys.exit(1)    

"""
    # QUARTET
def bit_mask(focal,ref):
    """
    #Used by partition_test
    
    #Generic function to create bitmask corresponding to a particular bipartition. "focal" is a list 
    #of tips on one side of a bipartition, while "ref" is a list of all tips in a tree
"""
    bitmask = []
    for i in ref:
        if i == ref[0]:
            bitmask.append(1)
        elif (i in focal) == (ref[0] in focal):
            bitmask.append(1)
        else:
            bitmask.append(0)
    return bitmask
"""

def treelength_test(args, tree_data):
    """
    Calculates mean treelength for one posterior distribution
    """
    try:
        sum = 0.
        for tr in tree_data:
            sum += tr.length()
        mean_tl = sum/len(tree_data)
        
        return mean_tl
    
    except:
        print """
    Problem calculating mean treelength test statistic...
        """
        if args.debug:
            traceback.print_exc()
        sys.exit(1)

def mean(vals):
    """
    Calculates the mean of a list of numbers.
    """
    return float(sum(vals))/float(len(vals))

def variance(vals):
    """
    Calculates the variance of a list of numbers.
    """
    sumSquares = 0.0
    meanVal = mean(vals)
    for i in vals:
        sumSquares += math.pow((i-meanVal),2)
    return sumSquares/float(len(vals))

def tlVar_test(args, tree_data):
    """
    Calculates the variance in treelength across one posterior distribution
    """
    try:
        tls = []
        [tls.append(tree.length()) for tree in tree_data]

        return variance(tls)
    
    except:
        print """
    Problem calculating treelength variance test statistic...
        """
        if args.debug:
            traceback.print_exc()
        sys.exit(1)

def factorial(y, x = 1):
    """
    Calculate product of integers i s.t. x < i <= y
    e.g. factorial(5, 1) = factorial(5) = 120, factorial(5,2) = 60
    """
    a = int(min([x, y]))
    b = int(max([x, y]))
    factorial = 1
    for i in range(a + 1, b + 1):
        factorial *= i
    return int(factorial)
    
###############  End Test Statistic Functions ###############

###########  Begin Parsing Functions and Classes ############

class QuantileAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        vals = values.split(',')
        quant_focal_breaks = []
        quant_bin_nos = []

        for i, val in enumerate(vals):
            if i % 2 == 0:
                quant_focal_breaks.append(int(val))
            else:
                quant_bin_nos.append(int(val))
        if not len(vals) % 2 == 0:
            raise InputError("Invalid quantiles")
        if not all([quant_focal_breaks[i] < quant_bin_nos[i] for i in range(len(quant_focal_breaks))]):
            raise InputError("All focal quantiles must be smaller than the corresponding overall number of bins")
        setattr(namespace, 'quant_focal_breaks', quant_focal_breaks)
        setattr(namespace, 'quant_bin_nos', quant_bin_nos)
        setattr(namespace, self.dest, True)
    
class PartitionAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if values is not None:
            part_list = values.split(',')
        else:
            part_list = []
        setattr(namespace, self.dest, part_list)

def sigint_handler(x,y):
    print """
    
    Program execution interrupted by the user.  Exiting..."""
    sys.exit(1)

def parse_input(argv):
    '''Parse command line input'''
    parser = argparse.ArgumentParser(prog='AMP', description='Assessing phylogenetic Model fit with Posterior prediction', 
        formatter_class=argparse.RawTextHelpFormatter, epilog=  'Defaults:\t\tNo test statistics are turned on by default.\n'
                                                                '\t\t\tDefault burn-in is 0.')
    parser.set_defaults(burnin = 0, manual = True, quantile = False, quant_focal_breaks = [], quant_bin_nos = [])
    parser.add_argument('--version', action='version', version='%(prog)s {VERSION}'.format(VERSION = VERSION), help='Print program version')
    parser.add_argument('scriptname', type=str, help='Name of script being called (e.g. ./amp0.99.py)')
    parser.add_argument('basename', type=str,
        help='''The portion of the filename common to all analysis files.  Tree files should
have the following name structure:

<basename>_<treefile#>_<rep#>.t, 

where the parts within < and > should be substituted as necessary. This name can 
include a path if files are not in the same directory as this script. The treefiles 
resulting from analysis of the original (empirical) data should be named: 

<basename>_emp_<rep#>.t  

The rep# will not be used if only the bipartition-specific likelihood ratio test 
statistic is selected.  When using the bipartition-specific likelihood ratio test 
statistic, output ML tree files from constrained searches (only Garli supported right 
now) should have this structure: 

<basename>_<treefile#>_bp<constraint#>.<pos/neg>.constraint.best.tre, 

substituting pos or neg as appropriate in the name to specify a positive or negative 
constraint.  When using the bipartition-specific Bayes factor test statistic estimated 
using model-switch thermodynamic integration (e.g., in-house software written by JMB), 
output files for Bayes factors should be named:

<basename>_<treefile#>_bp<constraint#>.bf.out

and should contain the following line:

Estimated ln(Bayes Factor) = <ln(BF) value>

When using the bipartition-specific Bayes factor test based on marginal likelihoods
estimated with steppingstone sampling in MrBayes v3.2.1, two types of output files will
be used, based on runs positively or negatively constraining a particular branch. These
output files should have the form:

<basename>_<treefile#>.con<constraint#>.<pos/neg>.log

The average marginal likelihood (taken from the line containing the word "Mean") in each
log file will be used to calculate the Bayes factor.)''')
    parser.add_argument('ndatasets', type=int, help='Total number of posterior predictive datasets to be analyzed')
    parser.add_argument('nruns', type=int, 
        help='Number of replicate analyses run for each posterior predictive dataset.\n'
             'This value will be ignored if only the bipartition-specific\n'
             'likelihood ratio test statistic has been chosen.')
    test_stat_group = parser.add_argument_group('Test Statistic Options')
    test_stat_group.add_argument('-q', '--quantile', action=QuantileAction, help='Quantile-based test statistic (default = %(default)s)')
    test_stat_group.add_argument('-e', action='store_true', dest='entropy', help='Entropy-based test statistic (default = %(default)s)')
    test_stat_group.add_argument('-i', action='store_true', dest='iqr', help='Interquartile range test statistic (default = %(default)s)')
    test_stat_group.add_argument('-p', action=PartitionAction, dest='part_list', default=[], 
        help='Partition-specific entropy test statistic\n'
             'Requires taxon names on one side of partition (default = %(default)s)')
    test_stat_group.add_argument('-T', action='store_true', dest='length', help='Mean tree-length test statistic (default = %(default)s)')
    test_stat_group.add_argument('-V', action='store_true', dest='tlVar', help='Tree-length variance test statistic (default = %(default)s)')
    test_stat_group.add_argument('-L', type=int, default=0, dest='likeConstraints', 
        help='Bipartition-specific likelihood ratio\n'
             'Requires number of constraint trees used. (default = %(default)s)')
    test_stat_group.add_argument('-b', type=int, default=0, dest='bfConstraints', 
        help='Bipartition-specific Bayes factor\n'
             'Estimated via model-switch thermodynamic integration\n'
             'Requires number of constraint trees used. (default = %(default)s)')
    test_stat_group.add_argument('-B', type=int, default=0, dest='mbSSbfConstraints', 
        help='Bipartition-specific Bayes factor\n'
             'Estimated via steppingstone sampling of marginal likelihoods\n'
             'For positively and negatively constrained searches in MrBayes v3.2.1\n'
             'Requires number of constraint trees used. (default = %(default)s)')
    burnin_group = parser.add_mutually_exclusive_group()
    burnin_group.add_argument('-m', type=int, dest='burnin', help='-m and -c are mutually exclusive\n'
                                                                  'Manual burn-in  (default = %(default)s)')
    burnin_group.add_argument('-c', '--mrc', dest='manual', action='store_false', 
        help='Find burn-in values in MrConverge log files\n'
             'Requires log files named as: basename_dataset#.log')
    pvalue_group = parser.add_argument_group('P-value Type')
    pvalue_group.add_argument('-l', '--lower', action='store_true', help='Lower one-tailed p-value (default = %(default)s)')
    pvalue_group.add_argument('-u', '--upper', action='store_true', help='Upper one-tailed p-value (default = %(default)s)')
    pvalue_group.add_argument('-t', '--twotailed', action='store_true', help='Two-tailed p-value (default = %(default)s)')
    output_group = parser.add_argument_group('Output Options')
    output_group.add_argument('-o', type=str, dest='outfile', help='Direct output to a file (default = %(default)s)')
    output_group.add_argument('-v', action='store_true', help='Output test statistic values for all posterior predictive datasets (default = %(default)s)')
    parser.add_argument('--nworkers', type=int, default=0, help='Number of worker processes to start  (default = 1 worker per processor)')
    parser.add_argument('-d', '--debug', action='store_true', help='Turn debugging on for more verbose messages')
    parser.add_argument('--timeit', action='store_true', help='Display tree reading and stat calculating times')

    return parser.parse_args(sys.argv)

if __name__ == '__main__':
    main()
