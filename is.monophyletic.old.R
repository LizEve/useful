#couldn't figure out how to loop in R so I just went through one by one. so fun. 
library(ape)

setwd("~/bin/Squam/data_files/mstxrm/monophyl/")
#file = "concat_raxml_nbl.phy"
#tree = read.tree(file)
test = c("Pogona_vitticeps", "Chlamydosaurus_kingii", "Rankinia_adelaidensis", "Ctenophorus_isolepis")
anguimorpha= c("Heloderma_horridum","Heloderma_suspectum","Celestus_enneagrammus","Anniella_pulchra","Ophisaurus_apodus","Ophisaurus_ventralis","Elgaria_multicarinata","Xenosaurus_platycephalus","Xenosaurus_grandis","Lanthanotus_borneensis","Varanus_exanthematicus","Varanus_acanthurus","Varanus_salvator","Shinisaurus_crocodilurus")

iguania= c("Brookesia_brygooi","Chamaeleo_calyptratus","Uromastyx_aegyptus","Leiolepis_belliana","Hydrosaurus_sp","Physignathus_cocincinus","Chelosania_brunnea","Moloch_horridus","Hypsilurus_boydi","Physignathus_leseuri","Pogona_vitticeps","Chlamydosaurus_kingii","Rankinia_adelaidensis","Ctenophorus_isolepis","Calotes_emma","Acanthosaura_lepidogaster","Draco_blanfordii","Trapelus_agilis","Agama_agama","Phrynocephalus_mystaceus","Crotaphytus_collaris","Gambelia_wislizenii","Basiliscus_basiliscus","Corytophanes_cristatus","Dipsosaurus_dorsalis","Sauromalus_obesus","Brachylophus_fasciatus","Morunasaurus_annularis","Enyalioides_laticeps","Stenocercus_guentheri","Tropiduris_plica","Uranoscodon_superciliosus","Urostrophus_vautieri","Leiosaurus_catamarcensis","Pristidactylus_torquatus","Oplurus_cyclurus","Chalarodon_madagascariensis","Anolis_carolinensis","Uta_stansburiana","Sceloporus_variabilis","Petrosaurus_mearnsi","Uma_scoparia","Phrynosoma_platyrhinos","Polychrus_marmoratus","Phymaturus_palluma","Liolaemus_bellii","Liolaemus_elongatus","Leiocephalus_barahonensis")

serpentes= c("Leptotyphlops_humilis","Typhlops_jamaicensis","Liotyphlops_albirostris","Anilius_scytale","Tropidophis_haetianus","Trachyboa_boulengeri","Aspidites_melanocephalus","Python_molurus","Loxocemus_bicolor","Xenopeltis_unicolor","Acrochordus_granulatus","Xenodermus_javanicus","Pareas_hamptoni","Homalopsis_buccata","Naja_kaouthia","Notechis_scutatus","Laticauda_colubrina","Micrurus_fulvius","Aparallactus_werneri","Atractaspis_irregularis","Lycophidion_capense","Lamprophis_fuliginosus","Lampropeltis_getula","Trimorphodon_biscutatus","Coluber_constrictor","Sonora_semiannulata","Imantodes_cenchoa","Heterodon_platyrhinos","Diadophis_punctatus","Amphiesma_stolata","Xenochrophis_piscator","Afronatrix_anoscopus","Natrix_natrix","Thamnophis_marcianus","Daboia_russelli","Causus_defillippi","Azemiops_feae","Agkistrodon_contortrix","Lachesis_muta","Bothrops_asper","Casarea_dussumieri","Calabaria_reinhardtii","Ungaliophis_continentalis","Exiliboa_placata","Lichanura_trivirgata","Eryx_colubrinus","Boa_constrictor","Epicrates_striatus","Cylindrophis_rufus","Uropeltis_melanogaster")

toxicofera= c("Heloderma_horridum","Heloderma_suspectum","Celestus_enneagrammus","Anniella_pulchra","Ophisaurus_apodus","Ophisaurus_ventralis","Elgaria_multicarinata","Xenosaurus_platycephalus","Xenosaurus_grandis","Lanthanotus_borneensis","Varanus_exanthematicus","Varanus_acanthurus","Varanus_salvator","Shinisaurus_crocodilurus", "Brookesia_brygooi","Chamaeleo_calyptratus","Uromastyx_aegyptus","Leiolepis_belliana","Hydrosaurus_sp","Physignathus_cocincinus","Chelosania_brunnea","Moloch_horridus","Hypsilurus_boydi","Physignathus_leseuri","Pogona_vitticeps","Chlamydosaurus_kingii","Rankinia_adelaidensis","Ctenophorus_isolepis","Calotes_emma","Acanthosaura_lepidogaster","Draco_blanfordii","Trapelus_agilis","Agama_agama","Phrynocephalus_mystaceus","Crotaphytus_collaris","Gambelia_wislizenii","Basiliscus_basiliscus","Corytophanes_cristatus","Dipsosaurus_dorsalis","Sauromalus_obesus","Brachylophus_fasciatus","Morunasaurus_annularis","Enyalioides_laticeps","Stenocercus_guentheri","Tropiduris_plica","Uranoscodon_superciliosus","Urostrophus_vautieri","Leiosaurus_catamarcensis","Pristidactylus_torquatus","Oplurus_cyclurus","Chalarodon_madagascariensis","Anolis_carolinensis","Uta_stansburiana","Sceloporus_variabilis","Petrosaurus_mearnsi","Uma_scoparia","Phrynosoma_platyrhinos","Polychrus_marmoratus","Phymaturus_palluma","Liolaemus_bellii","Liolaemus_elongatus","Leiocephalus_barahonensis", "Leptotyphlops_humilis","Typhlops_jamaicensis","Liotyphlops_albirostris","Anilius_scytale","Tropidophis_haetianus","Trachyboa_boulengeri","Aspidites_melanocephalus","Python_molurus","Loxocemus_bicolor","Xenopeltis_unicolor","Acrochordus_granulatus","Xenodermus_javanicus","Pareas_hamptoni","Homalopsis_buccata","Naja_kaouthia","Notechis_scutatus","Laticauda_colubrina","Micrurus_fulvius","Aparallactus_werneri","Atractaspis_irregularis","Lycophidion_capense","Lamprophis_fuliginosus","Lampropeltis_getula","Trimorphodon_biscutatus","Coluber_constrictor","Sonora_semiannulata","Imantodes_cenchoa","Heterodon_platyrhinos","Diadophis_punctatus","Amphiesma_stolata","Xenochrophis_piscator","Afronatrix_anoscopus","Natrix_natrix","Thamnophis_marcianus","Daboia_russelli","Causus_defillippi","Azemiops_feae","Agkistrodon_contortrix","Lachesis_muta","Bothrops_asper","Casarea_dussumieri","Calabaria_reinhardtii","Ungaliophis_continentalis","Exiliboa_placata","Lichanura_trivirgata","Eryx_colubrinus","Boa_constrictor","Epicrates_striatus","Cylindrophis_rufus","Uropeltis_melanogaster")

not= c("Tupinambis_teguixin",  "Callopistes_maculatus", "Teius_teyou")

ADNP= "/Users/ChatNoir/bin/Squam/data_files/mstxrm/monophyl/ADNP_misstxremoved.phy"            
AHR= "/Users/ChatNoir/bin/Squam/data_files/mstxrm/monophyl/AHR_misstxremoved.phy"             
AKAP9= "/Users/ChatNoir/bin/Squam/data_files/mstxrm/monophyl/AKAP9_misstxremoved.phy"           
BACH1= "/Users/ChatNoir/bin/Squam/data_files/mstxrm/monophyl/BACH1_misstxremoved.phy"           
BDNF= "/Users/ChatNoir/bin/Squam/data_files/mstxrm/monophyl/BDNF_misstxremoved.phy"            
BHLHB2= "/Users/ChatNoir/bin/Squam/data_files/mstxrm/monophyl/BHLHB2_misstxremoved.phy"          
BMP2= "/Users/ChatNoir/bin/Squam/data_files/mstxrm/monophyl/BMP2_misstxremoved.phy"            
CAND1= "/Users/ChatNoir/bin/Squam/data_files/mstxrm/monophyl/CAND1_misstxremoved.phy"           
CARD4= "/Users/ChatNoir/bin/Squam/data_files/mstxrm/monophyl/CARD4_misstxremoved.phy"           
CILP= "/Users/ChatNoir/bin/Squam/data_files/mstxrm/monophyl/CILP_misstxremoved.phy"            
concat= "/Users/ChatNoir/bin/Squam/data_files/mstxrm/monophyl/concat_raxm_test_misstxremoved.phy"
CXCR4= "/Users/ChatNoir/bin/Squam/data_files/mstxrm/monophyl/CXCR4_misstxremoved.phy"           
DLL1= "/Users/ChatNoir/bin/Squam/data_files/mstxrm/monophyl/DLL1_misstxremoved.phy"            
ECEL= "/Users/ChatNoir/bin/Squam/data_files/mstxrm/monophyl/ECEL_misstxremoved.phy"            
ENC1= "/Users/ChatNoir/bin/Squam/data_files/mstxrm/monophyl/ENC1_misstxremoved.phy"            
FSHR= "/Users/ChatNoir/bin/Squam/data_files/mstxrm/monophyl/FSHR_misstxremoved.phy"            
FSTL5= "/Users/ChatNoir/bin/Squam/data_files/mstxrm/monophyl/FSTL5_misstxremoved.phy"           
GALR1= "/Users/ChatNoir/bin/Squam/data_files/mstxrm/monophyl/GALR1_misstxremoved.phy"           
GHSR= "/Users/ChatNoir/bin/Squam/data_files/mstxrm/monophyl/GHSR_misstxremoved.phy"            
GPR37= "/Users/ChatNoir/bin/Squam/data_files/mstxrm/monophyl/GPR37_misstxremoved.phy"           
HLCS= "/Users/ChatNoir/bin/Squam/data_files/mstxrm/monophyl/HLCS_misstxremoved.phy"            
INHIBA= "/Users/ChatNoir/bin/Squam/data_files/mstxrm/monophyl/INHIBA_misstxremoved.phy"          
LRRN1= "/Users/ChatNoir/bin/Squam/data_files/mstxrm/monophyl/LRRN1_misstxremoved.phy"           
LZTSS1= "/Users/ChatNoir/bin/Squam/data_files/mstxrm/monophyl/LZTSS1_misstxremoved.phy"          
MKL1= "/Users/ChatNoir/bin/Squam/data_files/mstxrm/monophyl/MKL1_misstxremoved.phy"            
MLL3= "/Users/ChatNoir/bin/Squam/data_files/mstxrm/monophyl/MLL3_misstxremoved.phy"            
MSH6= "/Users/ChatNoir/bin/Squam/data_files/mstxrm/monophyl/MSH6_misstxremoved.phy"            
NGFB= "/Users/ChatNoir/bin/Squam/data_files/mstxrm/monophyl/NGFB_misstxremoved.phy"            
NKTR= "/Users/ChatNoir/bin/Squam/data_files/mstxrm/monophyl/NKTR_misstxremoved.phy"            
NTF= "/Users/ChatNoir/bin/Squam/data_files/mstxrm/monophyl/NTF_misstxremoved.phy"             
PNN= "/Users/ChatNoir/bin/Squam/data_files/mstxrm/monophyl/PNN_misstxremoved.phy"             
PRLR= "/Users/ChatNoir/bin/Squam/data_files/mstxrm/monophyl/PRLR_misstxremoved.phy"            
PTGER4= "/Users/ChatNoir/bin/Squam/data_files/mstxrm/monophyl/PTGER4_misstxremoved.phy"          
PTPN= "/Users/ChatNoir/bin/Squam/data_files/mstxrm/monophyl/PTPN_misstxremoved.phy"            
R35= "/Users/ChatNoir/bin/Squam/data_files/mstxrm/monophyl/R35_misstxremoved.phy"             
RAG1= "/Users/ChatNoir/bin/Squam/data_files/mstxrm/monophyl/RAG1_misstxremoved.phy"            
SINCAIP= "/Users/ChatNoir/bin/Squam/data_files/mstxrm/monophyl/SINCAIP_misstxremoved.phy"         
SLC30A1= "/Users/ChatNoir/bin/Squam/data_files/mstxrm/monophyl/SLC30A1_misstxremoved.phy"         
SLC8A1= "/Users/ChatNoir/bin/Squam/data_files/mstxrm/monophyl/SLC8A1_misstxremoved.phy"          
SLC8A3= "/Users/ChatNoir/bin/Squam/data_files/mstxrm/monophyl/SLC8A3_misstxremoved.phy"          
TRAF6= "/Users/ChatNoir/bin/Squam/data_files/mstxrm/monophyl/TRAF6_misstxremoved.phy"           
UBN1= "/Users/ChatNoir/bin/Squam/data_files/mstxrm/monophyl/UBN1_misstxremoved.phy"            
VCPIP1= "/Users/ChatNoir/bin/Squam/data_files/mstxrm/monophyl/VCPIP1_misstxremoved.phy"          
ZEB2= "/Users/ChatNoir/bin/Squam/data_files/mstxrm/monophyl/ZEB2_misstxremoved.phy"            
ZFP36L1= "/Users/ChatNoir/bin/Squam/data_files/mstxrm/monophyl/ZFP36L1_misstxremoved.phy" 

tree = read.tree(ADNP)
yes=is.monophyletic (phy = tree , tips = test)
tox=is.monophyletic (phy = tree , tips = toxicofera)
ang=is.monophyletic (phy = tree , tips = anguimorpha)
serp=is.monophyletic (phy = tree , tips = serpentes)
ig=is.monophyletic (phy = tree , tips = iguania)

yes
tox
ang
serp
ig

tree = read.tree(AHR)
yes=is.monophyletic (phy = tree , tips = test)
tox=is.monophyletic (phy = tree , tips = toxicofera)
ang=is.monophyletic (phy = tree , tips = anguimorpha)
serp=is.monophyletic (phy = tree , tips = serpentes)
ig=is.monophyletic (phy = tree , tips = iguania)

yes
tox
ang
serp
ig

tree = read.tree(AKAP9)
yes=is.monophyletic (phy = tree , tips = test)
tox=is.monophyletic (phy = tree , tips = toxicofera)
ang=is.monophyletic (phy = tree , tips = anguimorpha)
serp=is.monophyletic (phy = tree , tips = serpentes)
ig=is.monophyletic (phy = tree , tips = iguania)

yes
tox
ang
serp
ig

tree = read.tree(BACH1)
yes=is.monophyletic (phy = tree , tips = test)
tox=is.monophyletic (phy = tree , tips = toxicofera)
ang=is.monophyletic (phy = tree , tips = anguimorpha)
serp=is.monophyletic (phy = tree , tips = serpentes)
ig=is.monophyletic (phy = tree , tips = iguania)

yes
tox
ang
serp
ig

tree = read.tree(BDNF)
yes=is.monophyletic (phy = tree , tips = test)
tox=is.monophyletic (phy = tree , tips = toxicofera)
ang=is.monophyletic (phy = tree , tips = anguimorpha)
serp=is.monophyletic (phy = tree , tips = serpentes)
ig=is.monophyletic (phy = tree , tips = iguania)

yes
tox
ang
serp
ig

tree = read.tree(BHLHB2)
yes=is.monophyletic (phy = tree , tips = test)
tox=is.monophyletic (phy = tree , tips = toxicofera)
ang=is.monophyletic (phy = tree , tips = anguimorpha)
serp=is.monophyletic (phy = tree , tips = serpentes)
ig=is.monophyletic (phy = tree , tips = iguania)

yes
tox
ang
serp
ig

tree = read.tree(BMP2)
yes=is.monophyletic (phy = tree , tips = test)
tox=is.monophyletic (phy = tree , tips = toxicofera)
ang=is.monophyletic (phy = tree , tips = anguimorpha)
serp=is.monophyletic (phy = tree , tips = serpentes)
ig=is.monophyletic (phy = tree , tips = iguania)

yes
tox
ang
serp
ig

tree = read.tree(CAND1)
yes=is.monophyletic (phy = tree , tips = test)
tox=is.monophyletic (phy = tree , tips = toxicofera)
ang=is.monophyletic (phy = tree , tips = anguimorpha)
serp=is.monophyletic (phy = tree , tips = serpentes)
ig=is.monophyletic (phy = tree , tips = iguania)

yes
tox
ang
serp
ig

tree = read.tree(CARD4)
yes=is.monophyletic (phy = tree , tips = test)
tox=is.monophyletic (phy = tree , tips = toxicofera)
ang=is.monophyletic (phy = tree , tips = anguimorpha)
serp=is.monophyletic (phy = tree , tips = serpentes)
ig=is.monophyletic (phy = tree , tips = iguania)

yes
tox
ang
serp
ig

tree = read.tree(CILP)
yes=is.monophyletic (phy = tree , tips = test)
tox=is.monophyletic (phy = tree , tips = toxicofera)
ang=is.monophyletic (phy = tree , tips = anguimorpha)
serp=is.monophyletic (phy = tree , tips = serpentes)
ig=is.monophyletic (phy = tree , tips = iguania)

yes
tox
ang
serp
ig

tree = read.tree(concat)
yes=is.monophyletic (phy = tree , tips = test)
tox=is.monophyletic (phy = tree , tips = toxicofera)
ang=is.monophyletic (phy = tree , tips = anguimorpha)
serp=is.monophyletic (phy = tree , tips = serpentes)
ig=is.monophyletic (phy = tree , tips = iguania)

yes
tox
ang
serp
ig

tree = read.tree(CXCR4)
yes=is.monophyletic (phy = tree , tips = test)
tox=is.monophyletic (phy = tree , tips = toxicofera)
ang=is.monophyletic (phy = tree , tips = anguimorpha)
serp=is.monophyletic (phy = tree , tips = serpentes)
ig=is.monophyletic (phy = tree , tips = iguania)

yes
tox
ang
serp
ig

tree = read.tree(DLL1)
yes=is.monophyletic (phy = tree , tips = test)
tox=is.monophyletic (phy = tree , tips = toxicofera)
ang=is.monophyletic (phy = tree , tips = anguimorpha)
serp=is.monophyletic (phy = tree , tips = serpentes)
ig=is.monophyletic (phy = tree , tips = iguania)

yes
tox
ang
serp
ig

tree = read.tree(ECEL)
yes=is.monophyletic (phy = tree , tips = test)
tox=is.monophyletic (phy = tree , tips = toxicofera)
ang=is.monophyletic (phy = tree , tips = anguimorpha)
serp=is.monophyletic (phy = tree , tips = serpentes)
ig=is.monophyletic (phy = tree , tips = iguania)

yes
tox
ang
serp
ig

tree = read.tree(ENC1)
yes=is.monophyletic (phy = tree , tips = test)
tox=is.monophyletic (phy = tree , tips = toxicofera)
ang=is.monophyletic (phy = tree , tips = anguimorpha)
serp=is.monophyletic (phy = tree , tips = serpentes)
ig=is.monophyletic (phy = tree , tips = iguania)

yes
tox
ang
serp
ig

tree = read.tree(FSHR)
yes=is.monophyletic (phy = tree , tips = test)
tox=is.monophyletic (phy = tree , tips = toxicofera)
ang=is.monophyletic (phy = tree , tips = anguimorpha)
serp=is.monophyletic (phy = tree , tips = serpentes)
ig=is.monophyletic (phy = tree , tips = iguania)

yes
tox
ang
serp
ig

tree = read.tree(FSTL5)
yes=is.monophyletic (phy = tree , tips = test)
tox=is.monophyletic (phy = tree , tips = toxicofera)
ang=is.monophyletic (phy = tree , tips = anguimorpha)
serp=is.monophyletic (phy = tree , tips = serpentes)
ig=is.monophyletic (phy = tree , tips = iguania)

yes
tox
ang
serp
ig

tree = read.tree(GALR1)
yes=is.monophyletic (phy = tree , tips = test)
tox=is.monophyletic (phy = tree , tips = toxicofera)
ang=is.monophyletic (phy = tree , tips = anguimorpha)
serp=is.monophyletic (phy = tree , tips = serpentes)
ig=is.monophyletic (phy = tree , tips = iguania)

yes
tox
ang
serp
ig

tree = read.tree(GHSR)
yes=is.monophyletic (phy = tree , tips = test)
tox=is.monophyletic (phy = tree , tips = toxicofera)
ang=is.monophyletic (phy = tree , tips = anguimorpha)
serp=is.monophyletic (phy = tree , tips = serpentes)
ig=is.monophyletic (phy = tree , tips = iguania)

yes
tox
ang
serp
ig

tree = read.tree(GPR37)
yes=is.monophyletic (phy = tree , tips = test)
tox=is.monophyletic (phy = tree , tips = toxicofera)
ang=is.monophyletic (phy = tree , tips = anguimorpha)
serp=is.monophyletic (phy = tree , tips = serpentes)
ig=is.monophyletic (phy = tree , tips = iguania)

yes
tox
ang
serp
ig

tree = read.tree(HLCS)
yes=is.monophyletic (phy = tree , tips = test)
tox=is.monophyletic (phy = tree , tips = toxicofera)
ang=is.monophyletic (phy = tree , tips = anguimorpha)
serp=is.monophyletic (phy = tree , tips = serpentes)
ig=is.monophyletic (phy = tree , tips = iguania)

yes
tox
ang
serp
ig

tree = read.tree(INHIBA)
yes=is.monophyletic (phy = tree , tips = test)
tox=is.monophyletic (phy = tree , tips = toxicofera)
ang=is.monophyletic (phy = tree , tips = anguimorpha)
serp=is.monophyletic (phy = tree , tips = serpentes)
ig=is.monophyletic (phy = tree , tips = iguania)

yes
tox
ang
serp
ig

tree = read.tree(LRRN1)
yes=is.monophyletic (phy = tree , tips = test)
tox=is.monophyletic (phy = tree , tips = toxicofera)
ang=is.monophyletic (phy = tree , tips = anguimorpha)
serp=is.monophyletic (phy = tree , tips = serpentes)
ig=is.monophyletic (phy = tree , tips = iguania)

yes
tox
ang
serp
ig

tree = read.tree(LZTSS1)
yes=is.monophyletic (phy = tree , tips = test)
tox=is.monophyletic (phy = tree , tips = toxicofera)
ang=is.monophyletic (phy = tree , tips = anguimorpha)
serp=is.monophyletic (phy = tree , tips = serpentes)
ig=is.monophyletic (phy = tree , tips = iguania)

yes
tox
ang
serp
ig

tree = read.tree(MKL1)
yes=is.monophyletic (phy = tree , tips = test)
tox=is.monophyletic (phy = tree , tips = toxicofera)
ang=is.monophyletic (phy = tree , tips = anguimorpha)
serp=is.monophyletic (phy = tree , tips = serpentes)
ig=is.monophyletic (phy = tree , tips = iguania)

yes
tox
ang
serp
ig

tree = read.tree(MLL3)
yes=is.monophyletic (phy = tree , tips = test)
tox=is.monophyletic (phy = tree , tips = toxicofera)
ang=is.monophyletic (phy = tree , tips = anguimorpha)
serp=is.monophyletic (phy = tree , tips = serpentes)
ig=is.monophyletic (phy = tree , tips = iguania)

yes
tox
ang
serp
ig

tree = read.tree(MSH6)
yes=is.monophyletic (phy = tree , tips = test)
tox=is.monophyletic (phy = tree , tips = toxicofera)
ang=is.monophyletic (phy = tree , tips = anguimorpha)
serp=is.monophyletic (phy = tree , tips = serpentes)
ig=is.monophyletic (phy = tree , tips = iguania)

yes
tox
ang
serp
ig

tree = read.tree(NGFB)
yes=is.monophyletic (phy = tree , tips = test)
tox=is.monophyletic (phy = tree , tips = toxicofera)
ang=is.monophyletic (phy = tree , tips = anguimorpha)
serp=is.monophyletic (phy = tree , tips = serpentes)
ig=is.monophyletic (phy = tree , tips = iguania)

yes
tox
ang
serp
ig

tree = read.tree(NKTR)
yes=is.monophyletic (phy = tree , tips = test)
tox=is.monophyletic (phy = tree , tips = toxicofera)
ang=is.monophyletic (phy = tree , tips = anguimorpha)
serp=is.monophyletic (phy = tree , tips = serpentes)
ig=is.monophyletic (phy = tree , tips = iguania)

yes
tox
ang
serp
ig

tree = read.tree(NTF)
yes=is.monophyletic (phy = tree , tips = test)
tox=is.monophyletic (phy = tree , tips = toxicofera)
ang=is.monophyletic (phy = tree , tips = anguimorpha)
serp=is.monophyletic (phy = tree , tips = serpentes)
ig=is.monophyletic (phy = tree , tips = iguania)

yes
tox
ang
serp
ig

tree = read.tree(PNN)
yes=is.monophyletic (phy = tree , tips = test)
tox=is.monophyletic (phy = tree , tips = toxicofera)
ang=is.monophyletic (phy = tree , tips = anguimorpha)
serp=is.monophyletic (phy = tree , tips = serpentes)
ig=is.monophyletic (phy = tree , tips = iguania)

yes
tox
ang
serp
ig

tree = read.tree(PRLR)
yes=is.monophyletic (phy = tree , tips = test)
tox=is.monophyletic (phy = tree , tips = toxicofera)
ang=is.monophyletic (phy = tree , tips = anguimorpha)
serp=is.monophyletic (phy = tree , tips = serpentes)
ig=is.monophyletic (phy = tree , tips = iguania)

yes
tox
ang
serp
ig

tree = read.tree(PTGER4)
yes=is.monophyletic (phy = tree , tips = test)
tox=is.monophyletic (phy = tree , tips = toxicofera)
ang=is.monophyletic (phy = tree , tips = anguimorpha)
serp=is.monophyletic (phy = tree , tips = serpentes)
ig=is.monophyletic (phy = tree , tips = iguania)

yes
tox
ang
serp
ig

tree = read.tree(PTPN)
yes=is.monophyletic (phy = tree , tips = test)
tox=is.monophyletic (phy = tree , tips = toxicofera)
ang=is.monophyletic (phy = tree , tips = anguimorpha)
serp=is.monophyletic (phy = tree , tips = serpentes)
ig=is.monophyletic (phy = tree , tips = iguania)

yes
tox
ang
serp
ig

tree = read.tree(R35)
yes=is.monophyletic (phy = tree , tips = test)
tox=is.monophyletic (phy = tree , tips = toxicofera)
ang=is.monophyletic (phy = tree , tips = anguimorpha)
serp=is.monophyletic (phy = tree , tips = serpentes)
ig=is.monophyletic (phy = tree , tips = iguania)

yes
tox
ang
serp
ig

tree = read.tree(RAG1)
yes=is.monophyletic (phy = tree , tips = test)
tox=is.monophyletic (phy = tree , tips = toxicofera)
ang=is.monophyletic (phy = tree , tips = anguimorpha)
serp=is.monophyletic (phy = tree , tips = serpentes)
ig=is.monophyletic (phy = tree , tips = iguania)

yes
tox
ang
serp
ig

tree = read.tree(SINCAIP)
yes=is.monophyletic (phy = tree , tips = test)
tox=is.monophyletic (phy = tree , tips = toxicofera)
ang=is.monophyletic (phy = tree , tips = anguimorpha)
serp=is.monophyletic (phy = tree , tips = serpentes)
ig=is.monophyletic (phy = tree , tips = iguania)

yes
tox
ang
serp
ig

tree = read.tree(SLC30A1)
yes=is.monophyletic (phy = tree , tips = test)
tox=is.monophyletic (phy = tree , tips = toxicofera)
ang=is.monophyletic (phy = tree , tips = anguimorpha)
serp=is.monophyletic (phy = tree , tips = serpentes)
ig=is.monophyletic (phy = tree , tips = iguania)

yes
tox
ang
serp
ig

tree = read.tree(SLC8A1)
yes=is.monophyletic (phy = tree , tips = test)
tox=is.monophyletic (phy = tree , tips = toxicofera)
ang=is.monophyletic (phy = tree , tips = anguimorpha)
serp=is.monophyletic (phy = tree , tips = serpentes)
ig=is.monophyletic (phy = tree , tips = iguania)

yes
tox
ang
serp
ig

tree = read.tree(SLC8A3)
yes=is.monophyletic (phy = tree , tips = test)
tox=is.monophyletic (phy = tree , tips = toxicofera)
ang=is.monophyletic (phy = tree , tips = anguimorpha)
serp=is.monophyletic (phy = tree , tips = serpentes)
ig=is.monophyletic (phy = tree , tips = iguania)

yes
tox
ang
serp
ig

tree = read.tree(TRAF6)
yes=is.monophyletic (phy = tree , tips = test)
tox=is.monophyletic (phy = tree , tips = toxicofera)
ang=is.monophyletic (phy = tree , tips = anguimorpha)
serp=is.monophyletic (phy = tree , tips = serpentes)
ig=is.monophyletic (phy = tree , tips = iguania)

yes
tox
ang
serp
ig

tree = read.tree(UBN1)
yes=is.monophyletic (phy = tree , tips = test)
tox=is.monophyletic (phy = tree , tips = toxicofera)
ang=is.monophyletic (phy = tree , tips = anguimorpha)
serp=is.monophyletic (phy = tree , tips = serpentes)
ig=is.monophyletic (phy = tree , tips = iguania)

yes
tox
ang
serp
ig

tree = read.tree(VCPIP1)
yes=is.monophyletic (phy = tree , tips = test)
tox=is.monophyletic (phy = tree , tips = toxicofera)
ang=is.monophyletic (phy = tree , tips = anguimorpha)
serp=is.monophyletic (phy = tree , tips = serpentes)
ig=is.monophyletic (phy = tree , tips = iguania)

yes
tox
ang
serp
ig

tree = read.tree(ZEB2)
yes=is.monophyletic (phy = tree , tips = test)
tox=is.monophyletic (phy = tree , tips = toxicofera)
ang=is.monophyletic (phy = tree , tips = anguimorpha)
serp=is.monophyletic (phy = tree , tips = serpentes)
ig=is.monophyletic (phy = tree , tips = iguania)

yes
tox
ang
serp
ig

tree = read.tree(ZFP36L1)
yes=is.monophyletic (phy = tree , tips = test)
tox=is.monophyletic (phy = tree , tips = toxicofera)
ang=is.monophyletic (phy = tree , tips = anguimorpha)
serp=is.monophyletic (phy = tree , tips = serpentes)
ig=is.monophyletic (phy = tree , tips = iguania)

yes
tox
ang
serp
ig



yes=is.monophyletic (phy = tree , tips = test)
tox=is.monophyletic (phy = tree , tips = toxicofera)
ang=is.monophyletic (phy = tree , tips = anguimorpha)
serp=is.monophyletic (phy = tree , tips = serpentes)
ig=is.monophyletic (phy = tree , tips = iguania)
nope=is.monophyletic (phy = tree , tips = not)
yes
tox
ang
serp
ig
nope

tree$tip.label

files = list.files('~/bin/Squam/data_files/mstxrm/monophyl',pattern='misstxremoved.phy',full.names=T)
for(i in 1:length(files)){
	tree = read.tree(files[i])
	yes=is.monophyletic (phy = tree , tips = test)
	tox=is.monophyletic (phy = tree , tips = toxicofera)
	ang=is.monophyletic (phy = tree , tips = anguimorpha)
	serp=is.monophyletic (phy = tree , tips = serpentes)
	ig=is.monophyletic (phy = tree , tips = iguania)
	nope=is.monophyletic (phy = tree , tips = not)
	fnum=i
	fnum
	yes
	tox
	ang
	serp
	ig
	nope
}


library(ape)

setwd("~/bin/Squam/data_files/mstxrm/monophyl/")
test = c("Pogona_vitticeps", "Chlamydosaurus_kingii", "Rankinia_adelaidensis", "Ctenophorus_isolepis")



files = list.files('~/bin/Squam/data_files/mstxrm/monophyl',pattern='misstxremoved.phy',full.names=T, recursive=FALSE)
for(i in 1:length(files)){
	tree = read.tree(files[i])
	yes=is.monophyletic (phy = tree , tips = test)
	cat (yes, "/")
}
	




for(i in 1:length(files)){
	tree = read.tree(files[i])
	yes=is.monophyletic (phy = tree , tips = test)
	tox=is.monophyletic (phy = tree , tips = toxicofera)
	ang=is.monophyletic (phy = tree , tips = anguimorpha)
	serp=is.monophyletic (phy = tree , tips = serpentes)
	ig=is.monophyletic (phy = tree , tips = iguania)
	nope=is.monophyletic (phy = tree , tips = not)
	fnum=i
	info=c(fnum,yes,tox,ang,serp,ig,nope)
	write.table(info, "test.out" quote=F, row.names=F)
}
	

	
	{
		tree = read.tree(files[i])
		if is.monophyletic (phy = tree , tips = test)
		}