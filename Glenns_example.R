library(ape)

files = list.files('~/bin/Squam/data_files/mstxrm/clocklikepaup_mstxrm/outgroup_para',pattern='.phy',full.names=T)
outfiles = gsub('.phy','_outgroups.txt',files)

test_list= c('Sphenodon_punctatus','Homo_sapiens','Mus_musculus','Alligator_mississippiensis','Chelydra_serpentina','Crocodylus_porosus','Dromaius_novaehollandiae','Gallus_gallus','Podocnemis_expansa','Tachyglossus_aculeatus')



for(i in 1:length(files)){
	tmp = read.tree(files[i])
	if(!all(test_list %in% tmp$tip.label)){
		x = test_list[test_list %in% tmp$tip.label]
		write.table(x,file=outfiles[i],quote=F,row.names=F,col.names=F,sep='\t')	
	}
}




#%in% logical like ==, works with factors. for looking for multiple things within multiple things vector strings. 
 #! switches true and false

=

==
!=