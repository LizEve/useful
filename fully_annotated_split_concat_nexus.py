#This script is not useable, it is just annotated to understand what is going on
#script from bcf
from Bio.Nexus import Nexus 
#http://biopython.org/DIST/docs/api/Bio.Nexus.Nexus-module.html
#Nexus is a Package within BioPython, this is what Bio.Nexus refers to. 
#within this package there are submodules such as Bio.Nexus.Nexus - which is the nexus class
#within Module Nexus (Bio.Nexus import Nexus) there are classes and functions. http://biopython.org/DIST/docs/api/Bio.Nexus.Nexus-module.html
#one of the classes is also Nexus, which makes it slightly confusing. 
#Class Nexus - http://biopython.org/DIST/docs/api/Bio.Nexus.Nexus.Nexus-class.html

aln = Nexus.Nexus() #I think this is calling module nexus class nexus and assigning it to the variable aln. 
aln.read('squamate+cmosND2_char.nex') 
#This is what read does
def read(self, input): 
           """Read and parse NEXUS input (a filename, file-handle, or string).""" 
    
           # 1. Assume we have the name of a file in the execution dir or a 
           # file-like object. 
           # Note we need to add parsing of the path to dir/filename 
           try: 
               with File.as_handle(input, 'rU') as fp: 
                   file_contents = fp.read() 
                   self.filename = getattr(fp, 'name', 'Unknown_nexus_file') 
           except (TypeError, IOError, AttributeError): 
               #2 Assume we have a string from a fh.read() 
               if isinstance(input, basestring): 
                   file_contents = input 
                   self.filename = 'input_string' 
               else: 
                   print(input.strip()[:50]) 
                   raise NexusError('Unrecognized input: %s ...' % input[:100]) 
           file_contents = file_contents.strip() 
           if file_contents.startswith('#NEXUS'): 
               file_contents = file_contents[6:] 
           commandlines = _get_command_lines(file_contents) 
           # get rid of stupid 'NEXUS token - in merged treefiles, this might appear multiple times' 
           for i, cl in enumerate(commandlines): 
               try: 
                   if cl[:6].upper() == '#NEXUS': 
                       commandlines[i] = cl[6:].strip() 
               except: 
                   pass 
           # now loop through blocks (we parse only data in known blocks, thus ignoring non-block commands 
           nexus_block_gen = self._get_nexus_block(commandlines) 
           while True: 
               try: 
                   title, contents = next(nexus_block_gen) 
               except StopIteration: 
                   break 
               if title in KNOWN_NEXUS_BLOCKS: 
                   self._parse_nexus_block(title, contents) 
               else: 
                   self._unknown_nexus_block(title, contents) 

# assuming your partitions are defined in a charset block like:
#
# begin sets;
# charset bag2 = 1-186;
# charset bag3 = 187-483; 
# charset bche = 484-990;
# end;

# get count of charsets:
len(aln.charsets.keys())

# take a gander at the charsets:
#aln.charsets()

# split the concatenated file into charsets files (prepending whatever text you place after filename='')
aln.write_nexus_data_partitions(filename='ex', charpartition=aln.charsets)

# this will output in the os.getcwd():
# 
# test_bag2
# test_bag3
