# Grill & Chill

Jon Alberdi, Julen Galindo eta Jon Telleria-ren daw2-ko erronka

Django proyektu bat da.

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