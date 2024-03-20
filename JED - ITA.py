# Serpendeleev: Chimica 3330

from tkinter import *
import random

# Define the elements
elements = [
    "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne",
    "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca",
    "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga",
    "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr", "Nb",
    "Mo", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe",
    "Cs", "Ba", "La", "Ce", "Nd", "Eu","Gd", "Tb", "Er", "Yb",
    "Hf", "Ta", "W", "Os", "Ir", "Pt", "Au", "Hg", "Pb", "Bi",
    "Po", "Rn", "U", "Pu", "Fm", "Te", "In", "Te", "In", "Te", "In", 
]
#Gli elementi mancanti si potrebbero sbloccare con delle domande o raggiungendo un certo punteggio. Ogni dieta sblocca un certo elemento se raggiungi tot punti.
#  "Re", "Sc", "Tc", "Ru", "Rh", "Sm", "Pr", "Pm", "Tl", "Dy", "Ho", "Tm", "Lu", "At", "Fr", "Ra", "Ac", "Pa", "Np", "Am", "Cm", "Bk", "Cf", "Es", "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"

#Define diets
Diets_list = [
    "elementi della vita", #Isaac Asimov 'The Building Blocks of the Universe', Milan: A. Mondadori, 1971
    "elemeni dell'aria",
    "elementi critici", #Document 52020DC0474
    "elementi degli smartphone", #Figure 10 of https://doi.org/10.1016/j.jclepro.2023.138099
    "elementi del DNA", #https://edu.rsc.org/feature/elements-of-life/3007327.article
    "elementi radioattivi (serie di decadimento U-Th)", #Table 2 of https://doi.org/10.1016/B978-0-08-095975-7.00906-2
    "elementi considerati sicuri (grado A-E)\n in un reattore nucleare a fusione", #Figure 8 of https://doi.org/10.13182/FST19-1-146
    "elementi dedicati a scienziati", #http://www.liceorodolico.it/appunti/lim/IVF/SCIENZE/I%20nomi%20degli%20elementi%20e%20la%20loro%20origine-tottola%20biennio.pdf
    "elementi con nome di derivazione latina", #http://www.liceorodolico.it/appunti/lim/IVF/SCIENZE/I%20nomi%20degli%20elementi%20e%20la%20loro%20origine-tottola%20biennio.pdf
    "elementi con nome di derivazione greca", #http://www.liceorodolico.it/appunti/lim/IVF/SCIENZE/I%20nomi%20degli%20elementi%20e%20la%20loro%20origine-tottola%20biennio.pdf
    "elementi con nomi di città,\nstati, o di chissà dove", #http://www.liceorodolico.it/appunti/lim/IVF/SCIENZE/I%20nomi%20degli%20elementi%20e%20la%20loro%20origine-tottola%20biennio.pdf
    "elementi con nomi che non derivano nè dal latino, nè dal greco,\ne nemmeno da città o stati", #http://www.liceorodolico.it/appunti/lim/IVF/SCIENZE/I%20nomi%20degli%20elementi%20e%20la%20loro%20origine-tottola%20biennio.pdf
    "elementi allo stato solido alle condizioni standard di temperatura e pressione.", # https://ptable.com/?lang=it#Propriet%C3%A0
    "elementi allo stato liquido alle condizioni standard di temperatura e pressione.", # https://ptable.com/?lang=it#Propriet%C3%A0"solid elements at (choose the temperature) °C", # Check the elements on PTABLE: https://ptable.com/?lang=it#Propriet%C3%A0
    "elementi allo stato gassoso alle condizioni standard di temperatura e pressione.", # https://ptable.com/?lang=it#Propriet%C3%A0"liquid elements at (choose the temperature) °C", # Check the elements on PTABLE: https://ptable.com/?lang=it#Propriet%C3%A0
    "metalli",
    "non metalli",
    "elementi del primo gruppo (idrogeno & metalli alcalini)",
    "elementi del secondo gruppo (metalli alcalino terrosi)",
    "elementi del 15esimo gruppo (pnicogeni)",
    "elementi del gruppo XVI (calcogeni)",
    "elementi del gruppo XVII (alogeni)",
    "elementi del 18esimo gruppo (gas nobili)",
    "lantanoidi",
    "attinoidi",
    "metalli di transizione",
    "metalli post-transizione",
    "semimetalli",
    "non metalli reattivi",
    "elementi del blocco s",
    "elementi del blocco p",
    "elementi del blocco d",
    "elementi del blocco f",
    "elementi noti fin dai tempi antichi"
]

Elements_of_Diet = [
    ["O", "C", "H", "N", "P", "Ca", "S", "K", "Na", "Cl", "Mg", "Fe", "Zn", "Cr", "Co", "Cu", "Mn", "Mo", "Ni", "V", "Si", "B", "Se", "F", "I", "Br"],
    ["N", "O", "Ar", "C", "Ne", "He", "Kr", "Xe", "Rn"],
    ["Sb", "Ba", "Al", "Be", "Bi", "B", "Co", "F", "Ga", "Ge", "Hf", "In", "Li", "Mg","Nb","P", "Sc","Si","Sr","Ta","Ti","W","V"],
    ["Cu", "Al", "Ba", "Ni", "Ca", "Sn", "Fe", "Zn", "Ti", "Pb", "Ag", "Sr", "Au", "Mn", "Zr", "B", "Mg", "U", "Na", "W", "Cr", "Te", "Ge", "Ta", "Pd", "Nb", "Bi", "Ir", "Pt", "Li", "Y", "V", "Hf", "Be", "As", "In", "K", "Ga", "Co", "Sb", "Mo", "Sc", "Cd", "Re"],
    ["C", "H", "O", "N", "P"],
    ["U", "Th", "Pa", "Ra", "Rn", "Po", "Pb", "Bi", "Pu", "Ac", "Tl", "Am", "Np"],
    ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Mg", "Al", "Si", "P", "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr", "Fe", "Co", "Ni", "Cu", "Ge", "Se", "Kr", "Sr", "Y", "Ru", "Sn", "Te", "I", "Xe", "Cs", "Ba", "Ce", "Nd", "Sm", "Dy", "Yb", "Lu", "Tl"],
    ["Ge", "Sm", "Gd", "Bi", "Cm", "Es", "Fm", "Md", "No", "Lr", "Rf", "Sg", "Bh", "Mt", "Rg", "Og"],
    ["B", "C", "F", "Na", "Al", "Si", "S", "K", "Ca", "Sc", "Mn", "Fe", "Cu", "Ga", "Ge", "Rb", "Ru", "Pd", "In", "Sn", "Sb", "Te", "Cs", "La", "Ce", "Pm", "Eu", "Ho", "Tm", "Lu", "Hf", "Ta", "Ir", "Au", "Hg", "Pb", "Bi", "Po", "Rn", "Ra", "Np", "Cm", "Hs"],
    ["H", "He", "Li", "Be", "N", "O", "Ne", "P", "Cl", "Ar", "Ti", "Cr", "Co", "As", "Se", "Br", "Kr", "Nb", "Mo", "Tc", "Rh", "Ag", "Cd", "Sb", "I", "Xe", "Ba", "La", "Pr", "Nd", "Dy", "Os", "Tl", "Bi", "At", "Ac", "Pa", "U", "Pu"],
    ["Mg", "Sc", "Mn", "Ga", "Ge", "Se", "Sr", "Y", "Nb", "Tc", "Ru", "Pd", "Cd", "Te", "Eu", "Tb", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Re", "Bi", "Po", "Fr", "U", "Np", "Am", "Bk", "Cf", "Db", "Hs", "Ds"],
    ["V", "Ni", "Zn", "Zr", "Sb", "W", "Pt", "Th"],
    ["Li", "Be", "B", "C", "Na", "Mg", "Al", "Si", "P", "S",  "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Tl", "Pb", "Bi", "Po", "At", "Fr", "Ra", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr"],
    ["Hg", "Br"],
    ["H", "He", "N", "O", "F", "Ne","Cl", "Ar", "Kr", "Xe", "Rn"],
    ["Li", "Be", "Na", "Mg", "Al", "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr"],
    ["H", "He", "B", "C", "N", "O", "F", "Ne", "Si", "P", "S", "Cl", "Ar", "Ge", "As", "Se", "Br", "Kr", "Sb", "Te", "I", "Xe", "At", "Rn"],
    ["H", "Li", "Na", "K", "Rb", "Cs", "Fr"],
    ["Be", "Mg", "Ca", "Sr", "Ba", "Ra"],
    ["N", "P", "As", "Sb", "Bi", "Mc"],
    ["O", "S", "Se", "Te", "Po", "Lv"],
    ["F", "Cl", "Br", "I", "At", "Ts"],
    ["He", "Ne","Ar", "Kr", "Xe", "Rn", "Og"],
    ["La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu"],
    ["Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr"],
    ["Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn"],
    ["Al", "Ga", "In", "Sn", "Tl", "Pb", "Bi", "Po"],
    ["B", "Si", "Ge", "As", "Sb", "Te", "At"],
    ["H", "C", "N", "O", "F", "P", "S", "Cl", "Se", "Br", "I"],
    ["H", "He", "Li", "Be", "Na", "Mg", "K", "Ca", "Rb", "Sr", "Cs", "Ba", "Fr", "Ra"],
    ["B", "C", "N", "O", "F", "Ne", "Al", "Si", "P", "S", "Cl", "Ar", "Ga", "Ge", "As", "Se", "Br", "Kr", "In", "Sn", "Sb", "Te", "I", "Xe", "Tl", "Pb", "Bi", "Po", "At", "Rn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"],
    ["Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn"],
    ["La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No"],
    ["C", "Al", "S", "Ca", "Fe", "Cu", "As", "Ag", "Sn", "Sb", "Au", "Hg", "Pb"]#https://pubchem.ncbi.nlm.nih.gov/periodic-table/#property=YearDiscovered
]

Diet_Description = [
    ["\n\n\nOgni essere vivente, compreso l'uomo, è principalmente costituito da soli 11 elementi dei 90 presenti naturalemnte sulla Terra.\nSorprendente, vero?\n\n\n"],#(Isaac Asimov 'The Building Blocks of the Universe', Milan: A. Mondadori, 1971)
    ["\n\n\nSoltanto in seguito alle esperienze di Priestley e di Lavoisier (i quali misero in evidenza, il primo la presenza dell'ossigeno, ed il secondo che l'ossigeno si combinava col mercurio durante la combustione), che si poté stabilire che l'aria non era un corpo semplice.\n\n\n"],
    ["\n\nLe materie prime sono il cuore pulsante dell'economia europea, alimentando una vasta gamma di produzioni essenziali per la vita quotidiana e le tecnologie moderne. L'accesso affidabile a queste risorse vitali è una sfida crescente. Per affrontarla, l'UE ha identificato le materie prime critiche, fondamentali, ma a rischio.\n\n"], #https://single-market-economy.ec.europa.eu/sectors/raw-materials/areas-specific-interest/critical-raw-materials_en
    ["\n\n\nGli smartphone sono preziose risorse nella circolarità economica, contenendo elementi come oro, argento, platino e palladio. Tuttavia, il loro scarso riciclo ha impatti negativi sull'ambiente e sulla salute umana.\n\n\n"], #https://doi.org/10.1016/j.jclepro.2023.138099
    ["\n\n\n5 elementi compongono il linguaggio della vita.\n\n\n"],
    ["\n\n\nElevate concentrazioni di elementi radioattivi spesso derivano da attività umane, come l'estrazione e la lavorazione dell'uranio, e la combustione del carbone. Il combustibile nucleare esaurito rappresenta una vasta riserva di tali materiali.\n\n\n"],#https://doi.org/10.1016/B978-0-08-095975-7.00906-2"],
    ["\n\n\nQuesti materiali mirano a:\n- Ridurre al minimo il potenziale di causare malattie come il cancro.\n- Consentire il riciclo o lo smaltimento sicuro dei materiali esausti.\n- Agevolare la manutenzione senza compromettere la sicurezza.\n\n\n"], #doi:10.13182/fst19-1-146
    ["\n\n\nStoria degli elementi: da Mendeleev a Curie, una narrazione di scoperte e omaggi. La scienza rivela il suo tributo\n\n\n"],
    ["\n\n\nNomi come Carbonio (C), Ferro (Fe), e Oro (Au) sono testimoni dell'influenza del latino nella denominazione degli elementi chimici, rappresentando una connessione duratura tra la tradizione classica e la moderna scienza\n\n\n"],
    ["\n\n\nNomi come Idrogeno (H), Elio (He) e Litio (Li) sono testimonianza della ricca eredità della lingua greca nella denominazione degli elementi chimici, rappresentando una connessione antica tra la mitologia e la moderna scienza.\n\n\n"],
    ["\nMagnesio (Mg) prende il nome dalla città di Magnesia in Tessaglia, rinomata per la sua pietra purgativa. Scandio (Sc) deriva dal latino 'Scandia', che indica la Scandinavia, dove è stato per la prima volta isolato. Il selenio (Se) prende il suo nome dalla Luna, mentre il palladio (Pd) è dedicato all'asteroide Pallade. Questi elementi ci ricordano che la geografia degli elementi non ha confini!\n"],
    ["Vanadio (V) prende il nome da Vanadis, dea della bellezza nella mitologia norrena, per la bellezza e la varietà di colori dei suoi composti. Il nichel (Ni) deriva dal tedesco Kupfernickel, 'folletto del rame', perché i minatori sostenevano che impedissero loro di trovare il rame. Lo zirconio (Zr) deriva dall'arabo zerqun, 'colore dorato', a sua volta dal persiano azargun, composto da azar, 'fuoco', e gun, 'colore'. Il torio (Th) prende il nome da Thor, il dio del tuono nella mitologia norrena. Questi elementi ci ricordano che la geografia degli elementi non ha confini, ma si estende attraverso miti e culture, riflettendo la bellezza e la varietà del mondo che ci circonda.\n\n\n"],
    ["\n\n\nPlatone attribuì alla terra, che appare costantemente immobile, la forma del cubo poiché, per essere messa in movimento, questo solido richiede una spinta vigorosa."],
    ["\n\n\nIl bromo è un liquido\nrosso, ossidante,\nd'odor sgradevole\ne penetrante. (Alberto Cavaliere, Chimica in versi)\n\n\n"],
    ["\n\n\nPlatone attribuì all'aria la forma dell'ottaedro, poiché questo solido, composto da due piramidi, rappresenta efficacemente la sua natura dinamica\n\n\n"],
    ["I metalli possiedono molte proprietà distintive, come la formazione di cloruri e ossidi, la facilità di riduzione e la sostituzione dell'idrogeno negli acidi diluiti. Anche se, tecnicamente, il francio potrebbe avere il primato in base a questi criteri, la sua estrema instabilità e rarità lo escludono dalla classifica, pertanto, di solito, il primato viene assegnato al cesio."],
    ["\n\n\nLa maggior parte dei non metalli ha punti di fusione inferiori rispetto ai metalli, ma il carbonio costituisce un'eccezione in quanto ha un punto di fusione più alto rispetto agli altri non metalli e agli elementi in generale.\n\n\n"],
    ["\n\n\n'Che occorre diffidare del quasi uguale (il sodio è quasi uguale al potassio: ma col sodio non sarebbe successo nulla), del paranoicamente identico, del pressapoco, dell'oppure, di tutti i surrogati e di tutti i rappezzi. Le differenze possono essere piccole, ma portare a conseguenze radicalmente diverse, come gli aghi degli scambi; il mestiere del chimico consiste in buona parte nel quadrassi da queste differenze, nel conoscerle da vicino, nel prevederne gli effetti. Non solo il mestiere del chimico\n\n\n (Primo Levi, Il sistema periodico)"],
    ["\n\n\nHanno una reattività chimica relativamente alta e la tendenza a perdere due elettroni per formare ioni con carica positiva di +2.\n\nCuriosità: Nessuno più del berillio può essere 'incolpato' della lentezza dell'Universo nella formazione di nuovi elementi dopo il Big Bang. Questa specie atomica infatti è la prima della tavola periodica ad aver bisogno nel proprio nucleo di più neutroni che protoni (per poter essere stabile), e ciò ha determinato una minor velocità di formazione\n\n\n"],
    ["\n\n\n'Lo si classifica\nnel gruppo azoto,\nma qual metallico\ncorpo è più noto.\n\nBianco, ad un debole\nrosso tendente,\nl'aria non l'altera\nmenomamente.\n\n\n(Alberto Cavaliere, Chimica in versi)"],
    ["Questi elementi condividono caratteristiche simili, come la capacità di formare due legami covalenti, e si trovano nel sesto gruppo della tavola periodica.\n\nCuriosità: aii nostri occhi, e allo stato aeriforme, come sappiamo l'ossigeno molecolare dell'aria appare trasparente. Ma forse non tutti sanno che, sia in forma liquida sia in forma solida, l'ossigeno è invece di colore blu."],
    ["\n\n\nPosseggono sette elettroni nel guscio esterno e hanno una maggiore affinità elettronica rispetto agli altri elementi.\n\n\n"],
    ["Ci sono, nell'aria che respiriamo, i cosiddetti gas inerti. Portano curiosi nomi greci di derivazione dotta, che significano «il Nuovo», «il Nascosto», «l'Inoperoso», «lo Straniero». Sono, appunto, talmente inerti, talmente paghi della loro condizione, che non interferiscono in alcuna reazione chimica, non si combinano con alcun altro elemento, e proprio per questo motivo sono passati inosservati per secoli: solo nel 1962 un chimico di buona volontà, dopo lunghi ed ingegnosi sforzi, è riuscito a costringere lo Straniero (lo xenon) a combinarsi fugacemente con l'avidissimo, vivacissimo fluoro, e l'impresa è apparsa talmente straordinaria che gli è stato conferito il Premio Nobel. Si chiamano anche gas nobili, e qui ci sarebbe da discutere se veramente tutti i nobili siano inerti e tutti gli inerti siano nobili; si chiamano infine anche gas rari, benché uno di loro, l'argon, l'Inoperoso, sia presente nell'aria nella rispettabile proporzione dell'1 per cento: cioè venti o trenta volte più abbondante dell'anidride carbonica, senza la quale non ci sarebbe traccia di vita su questo pianeta. (Pirmo Levi, Il sistema periodico)"],
    ["Proprietà magnetiche: Alcuni lantanoidi, come il gadolinio, hanno proprietà magnetiche notevoli.\n\nLuminosità: Il lantanio è utilizzato in lampade agli alogenuri metallici.\n\nReattori nucleari: Il gadolinio è impiegato nei reattori nucleari come moderatore neutronico.\n\nColori: Alcuni lantanoidi sono noti per i loro colori intensi e vengono utilizzati in pigmenti per vernici e ceramiche.\n\nRarità: Alcuni lantanoidi, come l'europio e il terbio, sono piuttosto rari e vengono estratti da minerali specifici."],
    ["L'uranio, con numero atomico 92, è seguito dal nettunio e poi dal plutonio. Hai notato il parallelismo tra l'ordine di questi tre attinoidi e l'ordine dei tre corpi celesti nel nostro Sistema Solare? Si riflette nell'organizzazione dei Pianeti Urano e Nettuno, seguiti da Plutone, che è un Pianeta nano. Il mercurio, invece, sta da tutt'altra parte"],
    ["\n\n\nGià tutte le miniere sono magiche, da sempre. Le viscere della terra brulicano di gnomi, coboldi (cobalto!), niccoli (nichel!), che possono essere generosi e farti trovare il tesoro sotto la punta del piccone, o ingannarti, abbagliarti, facendo rilucere come l'oro la modesta pirite, o travestendo lo zinco con i panni dello stagno: e infatti, sono molti i minerali i cui nomi contengono radici che significano «inganno, frode, abbagliamento-\n\n\n(Primo Levi, Il sistema periodico)."],
    ["\n\n\nSiccome ho visto che queste questioni gli interessavano molto, gli ho spiegato che, se si va oltre le apparenze, il piombo è proprio il metallo della morte: perché fa morire, perché il suo peso è un desiderio di cadere, e cadere è dei cadaveri, perché il suo stesso colore è smorto-morto, perché è il metallo del pianeta Tuisto, che è il più lento dei pianeti, cioè il pianeta dei morti\n\n\n(Primo Levi, Il sistema periodico)"],
    ["\n\n\nBenché sia solido,\nnon è un metallo.\nE c'è, un arsenico\nbruno, uno giallo:\nquesto è sensibile\nmolto alla luce\ne l'altro arsenico\ntosto produce,\nmentre pel fosfor\ngià si notò\nche il giallo è stabile,\nma l'altro no. (Alvberto Cavaliere, Chimica in versi)"],
    ["Sono elementi chimici non metallici che mostrano una notevole reattività chimica, spesso formando composti con altri elementi attraverso legami covalenti o ionici. Questi elementi tendono a guadagnare elettroni durante le reazioni chimiche per raggiungere la stabilità elettronica. Esempi di reactive nonmetals includono ossigeno, cloro e fluoro."],
    ["Questi elementi sono noti come 'metalli alcalini' e 'metalli alcalino-terrosi'. Caratterizzati da una buona conducibilità elettrica e termica, hanno generalmente bassi punti di fusione e di ebollizione. Gli elementi del blocco s sono noti per formare facilmente cationi positivi perdendo uno o due elettroni dalla loro orbita esterna. Esempi di elementi del blocco s includono il litio, il sodio, il potassio, il calcio e il magnesio."],
    ["Questi elementi sono noti per la configurazione elettronica dei loro atomi che presenta elettroni negli orbitali p. Gli elementi del blocco p includono metalli, semimetalli e non metalli"],
    ["Sono caratterizzati dalla presenza di orbitali d parzialmente riempiti nei loro atomi. Gli elementi del blocco d sono generalmente solidi a temperatura ambiente, con punti di fusione ed ebollizione elevati."],
    ["Sono un gruppo di elementi chimici situati nella parte inferiore della tavola periodica, sotto il blocco d. Questi elementi sono noti come 'lantanoidi' e 'attinoidi' e sono caratterizzati dalla presenza di orbitali f parzialmente riempiti nei loro atomi. Molti elementi del blocco f sono radioattivi. Inoltre, alcuni lantanoidi, come il neodimio e il samario, sono utilizzati nella produzione di magneti permanenti ad alta potenza. Gli ioni di alcuni lantanoidi, come l'europio e il terbio, possono produrre intensi colori fluorescenti, rendendoli utili in applicazioni come le schermature televisive a colori e i tubi catodici."],
    ["Le prime tracce di lavorazione dell'oro risalgono a circa 6000 anni fa in Mesopotamia e in Egitto.\n\n\L'argento era utilizzato nelle monete già nell'antica Grecia e nell'antica Roma.\n\n\L'uso del ferro per la produzione di utensili e armi è stato fondamentale per lo sviluppo delle civiltà antiche, come quella greca e romana.\n\n\L'utilizzo dello stagno nella produzione di bronzo ha avuto un impatto significativo sull'evoluzione delle tecnologie metalliche nell'età del bronzo."]
]

# Constants for the game
SPEED = 100
SIZE = 20
PIECES = 3
SNAKE_COLOR = "#96AE21"
RAT_COLOR = "#E51A4B"
WINDOW_WIDTH = 620
WINDOW_HEIGHT = 520
BACKGROUND_COLOR = "#002F5F"

# Define the main menu options
main_menu_options = ["New Game", "Exit"]

# Create the main window
window = Tk()
window.title("Serpendeleev: Chimica 3330")
window.resizable(False, False)


# Function to ask for diet selection before starting a new game
def ask_for_diet_selection():
    diet_selection_window = Toplevel(window)
    diet_selection_window.title("Seleziona la dieta")
    diet_selection_window.geometry("300x100")

    selected_diet_var = StringVar(diet_selection_window)
    selected_diet_var.set(Diets_list[0])  # Set default value to the first diet in the list

    diet_dropdown = OptionMenu(diet_selection_window, selected_diet_var, *Diets_list)
    diet_dropdown.pack(pady=10)

    start_game_button = Button(diet_selection_window, text="Gioca", command=lambda: start_new_game(selected_diet_var.get(), diet_selection_window))
    start_game_button.pack()

def show_diet_description(selected_diet):
    index = Diets_list.index(selected_diet)
    description = Diet_Description[index]
    return description

# Function to start a new game
def start_new_game(selected_diet, window_to_close):
    window_to_close.destroy()  # Close the diet selection window
    window.after(5, clear_game_over_elements)
    canvas.delete("game_over_label") 
    global score, direction, diet
    score = 0
    direction = 'down'
    diet = selected_diet
    label.config(text="Serpendeleev è affamato di \n{}\nPunteggio: {}  |  Attento all'indio e al tellurio!".format(diet, round(score)))
    canvas.delete("all")
    snake = Snake()
    food = Food()
    next_turn(snake, food)

# Function to handle menu selection
def menu_action(selection):
    if selection == "New Game":
        ask_for_diet_selection()  # Ask for diet selection before starting the game
    elif selection == "Exit":
        window.destroy()

# Create a dropdown menu
menu_bar = Menu(window)
window.config(menu=menu_bar)

# Create a File menu
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
for option in main_menu_options:
    file_menu.add_command(label=option, command=lambda opt=option: menu_action(opt))



# Function to start a new game

# Create the score label
score = 0
direction = 'down'
diet = Diets_list [0]
label = Label(window, text="Serpendeleev è affamato di\n{}\n     Punteggio: {}  |  Attento all'indio e al tellurio!   ".format(diet, round(score)), font=('Corbel', SIZE))
label.pack()

# Create the canvas for the game
canvas = Canvas(window, bg=BACKGROUND_COLOR, height=WINDOW_HEIGHT, width=WINDOW_WIDTH)
canvas.pack()

# Create a dropdown menu
menu_bar = Menu(window)
window.config(menu=menu_bar)

# Create a File menu
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
for option in main_menu_options:
    file_menu.add_command(label=option, command=lambda opt=option: menu_action(opt))


# Define the Snake class
class Snake:

    def __init__(self):
        self.body_size = PIECES
        self.coordinates = []
        self.squares = []

        for i in range(0, PIECES):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SIZE, y + SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

# Define the Food class
class Food:

    # Define selectRandom function outside the class
    def selectRandom(self, elements):
        return random.choice(elements)

    def __init__(self):
        x = random.randint(0, (WINDOW_WIDTH / SIZE) - 1) * SIZE
        y = random.randint(0, (WINDOW_HEIGHT / SIZE) - 1) * SIZE

        self.coordinates = [x, y]

        elm = self.selectRandom(elements)  # Call selectRandom using self
        self.element_text = canvas.create_text(x + SIZE/2, y + SIZE/2, text=elm, fill=RAT_COLOR, font=('Corbel 18 bold'), tag="food")

def next_turn(snake, food):
    global space_pressed, score, diet

    if space_pressed:
        element_changed = canvas.itemcget(food.element_text, "text")

        #Balancing the scores so that continuously pressing the space bar does not give any advantage
        if element_changed in Elements_of_Diet[Diets_list.index(diet)]:
            score -= ((len(elements) - len(Elements_of_Diet[Diets_list.index(diet)]))/len(elements))*100
        else:
            score += (len(Elements_of_Diet[Diets_list.index(diet)])/len(elements))*100


        label.config(text="Serpendeleev è affamanto di \n{}\n     Punteggio: {}  |  Attento all'indio e al tellurio!   ".format(diet, round(score)))
        canvas.delete("food")
        food = Food()
        space_pressed = False  # Resetta la variabile space_pressed

    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SIZE
    elif direction == "down":
        y += SIZE
    elif direction == "left":
        x -= SIZE
    elif direction == "right":
        x += SIZE

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SIZE, y + SIZE, fill=SNAKE_COLOR)

    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1] and canvas.itemcget(food.element_text, "text") != "In" and canvas.itemcget(food.element_text, "text") != "Te":
        element_eaten = canvas.itemcget(food.element_text, "text")
        if element_eaten in Elements_of_Diet[Diets_list.index(diet)]:
            score += ((len(elements) - len(Elements_of_Diet[Diets_list.index(diet)]))/len(elements))*100
        else:
            score -= (len(Elements_of_Diet[Diets_list.index(diet)])/len(elements))*100
        label.config(text="Serpendeleev è affamato di \n{}\n     Punteggio: {}  |  Attento all'indio e al tellurio!   ".format(diet, round(score)))
        canvas.delete("food")
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake, food):
        game_over(diet)
    else:
        window.after(SPEED, next_turn, snake, food)



# Function to handle direction change
def change_direction(new_direction):
    global direction
    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

# Function to check for collisions
def check_collisions(snake, food):
    x, y = snake.coordinates[0]

    if x < 0 or x >= WINDOW_WIDTH:
        return True
    elif y < 0 or y >= WINDOW_HEIGHT:
        return True
    elif  (canvas.itemcget(food.element_text, "text") == "In" or canvas.itemcget(food.element_text, "text") == "Te") and x == food.coordinates[0] and y == food.coordinates[1]:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False

# Function to change food
def replace_food(event):
    global space_pressed
    space_pressed = True
window.bind('<space>', replace_food)

# Function to handle game over
def game_over(selected_diet):
    global game_over_label, diet_description_label

    canvas.delete(ALL)
    game_over_label = Label(canvas, text="[Stay Hungry] [Stay Periodic]", font=('Corbel', 30), fg=RAT_COLOR, bg=BACKGROUND_COLOR)
    game_over_label.pack(pady=20)
    diet_description = show_diet_description(selected_diet)
    diet_description_label = Text(canvas, wrap="word", font=('Corbel', 11), bg=BACKGROUND_COLOR, fg="white")
    diet_description_label.insert(END, diet_description)
    diet_description_label.pack(expand=True, fill=BOTH)
    

# Function to clear game over elements
def clear_game_over_elements():
    global game_over_label, diet_description_label

    if game_over_label:
        game_over_label.destroy()
        game_over_label = None
    if diet_description_label:
        diet_description_label.destroy()
        diet_description_label = None

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Bind keys for controlling the snake throughh arrow and leter. This provides flexibility in controlling the game, allowing players to choose their preferred control method.
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<KeyPress-a>', lambda event: change_direction('left'))
window.bind('<KeyPress-A>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<KeyPress-d>', lambda event: change_direction('right'))
window.bind('<KeyPress-D>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<KeyPress-w>', lambda event: change_direction('up'))
window.bind('<KeyPress-W>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))
window.bind('<KeyPress-s>', lambda event: change_direction('down'))
window.bind('<KeyPress-S>', lambda event: change_direction('down'))




snake = Snake()
food = Food()
space_pressed = False
next_turn(snake, food)
game_over_label = None
diet_description_label = None

# Run the main event loop
window.mainloop()
