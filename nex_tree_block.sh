#!/bin/bash
#May 19th 2015 GGM
#adjust 'for f in *' and 'gene=' depending on file name

outfile='genetrees.nex'
#-e flag enables reading of \characters
echo -e '#NEXUS\n\nBegin trees;\n\n' >> $outfile
for f in *.phy;
do
tree=`cat $f`
#gene=`echo $f | awk -F'_' '{ print $2}' |  awk -F'.' '{ print $1}' `  
gene=`echo $f | awk -F'_' '{ print $1}' `
echo -e 'tree '$gene' = [&U] '$tree >> $outfile
done


#Examples of use

#iterate and compile
outfile='misstxremoved_prunedog_genetrees.nex'
#-e flag enables reading of \characters
echo -e '#NEXUS\n\nBegin trees;\n\n' >> $outfile
for f in *.phy;
do
tree=`cat $f`
#gene=`echo $f | awk -F'_' '{ print $2}' |  awk -F'.' '{ print $1}' `  
gene=`echo $f | awk -F'_' '{ print $1}' `
echo -e 'tree '$gene' = [&U] '$tree >> $outfile
done
echo 'END;' >> $outfile

#single
outfile='concat_ADNP_misstxremoved.nex'
#-e flag enables reading of \characters
echo -e '#NEXUS\n\nBegin trees;\n\n' >> $outfile
f="concat_ADNPtaxa_nbl.phy"
tree=`cat $f`
#gene=`echo $f | awk -F'_' '{ print $2}' |  awk -F'.' '{ print $1}' `  
gene=`echo $f | awk -F'_' '{ print $1}' `
echo -e 'tree '$gene' = [&U] '$tree >> $outfile
echo 'END;' >> $outfile


#iterate and keep files seperate
