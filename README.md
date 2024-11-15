# Grill & Chill

Jon Alberdi, Julen Galindo eta Jon Telleria-ren daw2-ko erronka

Django proiektu bat da.

## Arkitektura

### Zerbitzariak
1. **Web Zerbitzaria (Zerbitzari 1)**: Erabiltzaileen eskaerak kudeatzen ditu eta web aplikazioa exekutatzen du.
2. **Datu-Base Zerbitzaria (Zerbitzari 2)**: Datu-basea ostatatzen du. Segurtasun arrazoiengatik, gomendatzen da zerbitzari hau zuzenean Interneten esposatuta ez egotea.
3. **Babes Zerbitzaria (Zerbitzari 3)**: Datu-basearen eta beste datu garrantzitsuen kopiak kudeatzen ditu.
![alt text](image.png)
### Zerbitzarien Firewall-a
- **Web Zerbitzaria**:
  - HTTP, HTTPS eta SSH trafikoa onartzen du.
  
- **Datu-Base Zerbitzaria**:
  - Web zerbitzaritik datorren MySQL sarrera soilik onartzen du eta SSH sarrera.

- **Back-up Zerbitzaria**:
  - Datu-Base zerbitzaritik segurtasunerako kopiak egiteko eta kudeaketarako SSH sarrera onartzen du.


### 1. Zerbitzari 1 (Web Zerbitzaria)
### 1. Zerbitzari 1 (Web Zerbitzaria)
### 1. Zerbitzari 1 (Web Zerbitzaria)
# WEBGUNEA

## Webgunearen Diseinu eta Egituraren Laburpena

### Prototipoa eta Edukien Antolaketa:
- **Testu eta Irudiak Kokatu**: CSS estiloek edukiak logikoki antolatzen dituzte, testuak eta irudiak banatuz. **Header** eta **nav** atalak gune nagusian kokatuta daude, logotipoa eta nabigazioa bistaratuz.
- **Maskarak eta Koloreak**: Atal nagusietan kolore desberdinak eta kontrasteak erabiltzen dira, `.karratua` klaseko estiloetan ikusgai, webgunea ikusgarri eta erakargarri egiteko.

### Egitura eta HTML Atalak:
- Web orriak HTML5 atalak erabiltzen ditu (**body**, **header**, **section**, **footer**) edukia modu logiko eta ondo antolatuan aurkezteko.
- Atal bakoitzak bere funtzioa du: goiburua (**header**), edukia (**section**, **article**) eta amaierako informazioa (**footer**).

### Osagai Interaktiboak:
- **Slider eta Karusela**: `.carousel` klaseak erabiltzen dira edukiak irristatzen erakusteko, eta erabiltzaileari eduki dinamikoa eta erakargarria eskaintzen diote.
- **Formularioak eta Akordeoiak**: Erabiltzaileek datuak sartzeko aukera dute (erregistro eta saio-hasiera orrialdeetan), eta akordeoi estiloko osagaiak edukiak zabaldu eta ixteko aukera ematen dute.
- **Txartel Estiloa**: `.products` eta `.about` klaseek txartel estiloko edukiak biltzen dituzte, produktuak eta informazioa bistaratuz modu erakargarri batean.

### Interaktibitatea eta Animazioak:
- **Hover eta Sarrerako Efektuak**: Esteketan eta produktuen GIFetan animazioak aplikatzen dira erabiltzailearen interakzioa erakargarriagoa egiteko.
- **Karusela eta Akordeoia**: Karuseleko elementuak leunki irristatzen dira, eta akordeoiak edukiak zabaltzeko eta ixteko aukera eskaintzen du.
- **Testu eta Multimedia Elementuak**: Gailu desberdinetara egokitzen dira, multimedia elementuak eta irudiak ikuspegi erakargarri batean txertatuz. Beste osagai batzuk, hala nola sare sozialetako ikonoak eta saskia, erabiltzailearen arreta erakartzeko gehitzen dira.

**Orokorrean**, CSS estiloak eta JavaScript animazioak modu koherentean aplikatzen dira, erabiltzaileak erraz nabigatu eta interakzio erakargarria izan dezan. Orrialde bakoitzaren egitura eta funtzionalitatea argi eta garbi definituta dago, eta webguneak estilo eta erabilgarritasun iraunkorra eskaintzen du.

---

## Fitxategien Deskribapena

1. **base.html** - Gune Orokorraren Oinarrizko Txantiloia
   - **HTML**: Gune osoko egitura definitzen du, goiburua, nabigazioa eta orri-oina barne.
   - **JavaScript Funtzionalitatea**:
     - **Hover Animazioak**: Nabigazio estekak hover egitean letra-tamaina handituz erabiltzaileen arreta erakartzen dute.

2. **register.html** - Erabiltzaile Erregistro Inprimakia
   - **HTML**: Erabiltzailearen datuak biltzeko inprimakia, izena, abizena, pasahitza, emaila, telefonoa eta helbidea jasotzen dituena.
   - **JavaScript Funtzionalitatea**:
     - **Nabigazio Animazioa**: Nabigazio-esteketan hover efektuak aplikatzen dira, tamaina handituz erabiltzailearentzako interakzio erakargarria sortzeko.
     - **Validazioak**: `validations.js` fitxategia erabiltzaileen sarrerak balioztatzeko eta errore mezuekin erabiltzaileari laguntzeko.

3. **index.html** - Hasierako Orria
   - **HTML**: Enpresaren aurkezpena eta produktuen deskribapen laburrak biltzen dituen hasierako orria.
   - **JavaScript Funtzionalitatea**:
     - **Sarrerako Efektua**: Orrialdean behera egiten denean, scroll efektuak GIF bat ezkerretara mugiarazten du, webgunea dinamikoa eginez.

4. **kontaktuak.html** - Kontaktua Orria
   - **HTML**: Enpresarekin harremanetan jartzeko orrialdea, Google Maps integrazioa ere badu.
   - **JavaScript Funtzionalitatea**: Nabigazio esteketan hover animazioa aplikatzen da hemen ere, estilo koherentea bermatzeko.

5. **logIn.html** - Saioa Hasteko Orria
   - **HTML**: Erabiltzailearen saioa hasteko formularioa.
   - **JavaScript Funtzionalitatea**:
     - **Hover Efektuak**: Nabigazio estekek animazioak dituzte hover egitean erabiltzailearen arreta erakartzeko.

6. **produktuak.html** - Produktuen Orrialdea
   - **HTML**: Produktuak kategoriatan antolatuta bistaratzen dira: hasierakoak, hanburgesak, postreak, eta edariak.
   - **JavaScript Funtzionalitatea**:
     - **Karusel eta Modalak**: Kategoria bakoitzeko produktuak zabaldu eta ixteko toggle funtzioak aplikatzen dira, modal eta karuselekin batera.
     - **Produktuen Kantitatea**: Produktu kopurua eguneratzeko aukera eskaintzen da.
     - **Hover eta Scroll Efektuak**: Produktuen GIFak horizontalki mugitzen dira erabiltzaileak behera egiten duen heinean, eta esteketan tamaina handitzen da hover egitean.

--- 

**Webguneak** erabiltzaile esperientzia erakargarria eta interaktiboa eskaintzen du, diseinu koherente eta funtzionalitate errazen bidez.
