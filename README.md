# Auto-Clicker Applicatie

Een automatische clicker applicatie waarmee je 3 posities op het scherm kunt selecteren door erop te klikken.

## Installatie

### Optie 1: Met Python (makkelijkste)
1. Zorg dat Python 3.x geïnstalleerd is
2. Dubbel-klik `install_dependencies.bat` om dependencies te installeren
3. Dubbel-klik `run.bat` om de app te starten

### Optie 2: Standalone executable bouwen
```bash
pip install cx_Freeze
python setup.py build
```

Dit maakt een `build/` folder met een standalone executable.

## Gebruik

1. Start de applicatie
2. Een semi-transparant venster verschijnt
3. Klik 3 keer op het scherm om de posities in te stellen
4. De website opent automatisch
5. Drie klikken worden uitgevoerd op de ingestelde posities
6. Druk `q` om het script te stoppen

## Files

- `main.py` - Hoofdscript
- `requirements.txt` - Python dependencies
- `setup.py` - Build configuratie voor executable
- `install_dependencies.bat` - Installation script voor Windows
- `run.bat` - Start script

## Vereisten

- Python 3.x
- Windows (macOS/Linux vereist aanpassingen)
- Admin-rechten (voor muisbesturing)
