Title: Dolní propust se směrovou odbočnicí pro 144MHz 
Date: 2009-07-23
Author: OK2AIA

Obvodový návrh dolní propust je
[převzat od OK1VPZ](http://www.ok2kkw.com/00003016/dp144/dp144.htm).
Obvodový návrh jsem zkontroloval ve standardním obvodovém
simulátoru typu Spice. Byly provedeny simulace jak frekvenční přenosové
charakteristiky tak i vstupní impedanční frekvenční charakteristiky.
Při variaci hodnot použitých prvků jsem zjistil, že vzhledem k použitým
kondenzátorům dosáhnu lepších parametrů, když se hodnoty vstupní a
výstupní indukčnosti zvýší z původních 55nH na 65nH a to přidáním ¼
závitu. Metodou variace jsem zjistil také citlivost přenosu a vstupní
impedance na hodnotách použitých prvků. Zde je důležitým závěrem, že je
třeba vždy nastavovat co nejlepší PSV na vstupu správně zatíženého
filtru při pracovním kmitočtu a pak má i frekvenční přenosová
charakteristika průběh, který se téměř neliší od požadovaného. Ve
filtru jsou použity SMD kondenzátory od firmy American Technical
Ceramics z řady 100B verze pro 500V. Právě parametry těchto
kondenzátorů jako maximální VF proud a ekvivalentní sériový odpor jsou
limitem pro výkonovou zatížitelnost filtru. Při jmenovitém výkonu
koncového stupně 350W je třeba vychladit ze SMD kondenzátoru ztrátový
výkon 800mW při trvalém zaklíčování.

Směrová odbočnice je mým vlastním návrhem. Vazební linky jsou z důvodu 
lepší citlivosti navrženy pro charakteristickou impedanci 100Ohm. 
Detekci urovně vyvázaného dopředného a odraženého výkonu zajišťují dva 
špičkové usměrňovače s použitím schottkyho diod. Poměrně solidní 
teoretickou analýzu týkající se směrových odbočnic lze najít na serveru
[http://kilyos.ee.bilkent.edu.tr/~microwave/](http://kilyos.ee.bilkent.edu.tr/~microwave/programs/magnetic/dcoupler/dcoupler.htm).

Na těchto stránkách najdeme také i on-line návhový nástroj, který jsem 
při své konstrukci využil. Je důležité upozornit, že tento návhový 
nástroj umožňuje analýzu a syntézu pouze pro planární struktury a nelze 
jej použít pro vlnovodové či koaxiální struktury. Zájemci si můžou 
výsledek z tohoto nástroje zkontrolovat v EM simulátoru vloženého do 
free verze Ansoft Designer SV, což je velmi solidní nástroj pro profi 
návrh RF a mikrovlnných struktur. Free verze obsahuje bohužel jen 
momentovou metodu výpočtu, takže je vhodná jen pro lineární a planární 
struktury. Ne pro 3D!!!

![Schéma](images/dolni_propust_144mhz/schema.jpg)

![Plošný spoj](images/dolni_propust_144mhz/pcb.jpg)

Dolnofrekvenční propusti byly realizovány na plošném spoji  tloušťky
1,5mm, jehož materiálem je laminát plněný teflonem od OK2EZ. Měření a
nastavení bylo provedeno na Mikrovlnném setkání ve Frenštátě za pomocí
měřicí techniky donesené Petrem OK2ULQ, za což mu velmi děkuji.

![Dolní propust 144Mhz](images/dolni_propust_144mhz/propust.jpg)

Z porovnání výsledků simulace a měření je viditelný rozdíl v útlumu 
filtru na kmitočtu 432MHz. Simulace dává přenos -84,7dB a měření pouze 
-60dB. Tento rozdíl je způsobený hlavně vlivem parazitní kapacity 
použitých indukčností a ekvivaletního sériového odporu použitých SMD 
kondenzátorů, protože tyto parametry nebyly při simulaci modelovány. 

Směrová odbočnice byla měřena jednoduchou metodou RF generátor, umělá 
zátěž 50Ohm na hlavním vedení a měření úrovně SS napětí za špičkovými 
usměrňovači. Následně byly úrovně detegovaných napětí přepočteny na 
vyvázané výkony. Po výpočtu vyšla vazba -29,1dB a směrovost -25,3dB na 
kmitočtu 144,2MHz. Tato směrová odbočnice by měla být schopná měřit PSV 
již od hodnoty 1,2, což je pro účely reflektometrické ochrany koncového 
stupně plně dostačující. Diody ve špičkových usměrňovačích vyvázaného 
výkonu jsou dimenzovány tak, že teoreticky je možno indikovat až výkony 
1.5kW.

Petr OK2AIA
