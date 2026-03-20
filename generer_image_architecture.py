"""
Script pour générer automatiquement l'image de l'architecture
Utilise l'API Mermaid.ink pour convertir le diagramme en image PNG
"""
import base64
import urllib.parse
import urllib.request
from pathlib import Path

def generer_image_architecture():
    """Génère l'image de l'architecture à partir du fichier .mmd"""
    
    # Chemin du fichier Mermaid
    mmd_file = Path(__file__).parent / "architecture_diagram.mmd"
    
    if not mmd_file.exists():
        print(f"❌ Fichier {mmd_file} introuvable")
        return
    
    # Lire le contenu du fichier
    with open(mmd_file, 'r', encoding='utf-8') as f:
        mermaid_code = f.read()
    
    print("📊 Génération de l'image de l'architecture...")
    print(f"📄 Source : {mmd_file}")
    
    # Méthode 1 : API Mermaid.ink (PNG via URL)
    try:
        # Encoder le code Mermaid en base64
        encoded = base64.urlsafe_b64encode(mermaid_code.encode('utf-8')).decode('ascii')
        
        # URL de l'API Mermaid.ink
        url = f"https://mermaid.ink/img/{encoded}"
        
        print(f"🌐 URL de l'image : {url}")
        
        # Télécharger l'image
        output_path = Path(__file__).parent / "architecture.png"
        
        print(f"⬇️  Téléchargement en cours...")
        urllib.request.urlretrieve(url, output_path)
        
        print(f"✅ Image générée : {output_path}")
        print(f"📏 Taille du fichier : {output_path.stat().st_size / 1024:.2f} Ko")
        
        # Générer aussi une version SVG (meilleure qualité)
        svg_url = f"https://mermaid.ink/svg/{encoded}"
        svg_output = Path(__file__).parent / "architecture.svg"
        
        urllib.request.urlretrieve(svg_url, svg_output)
        print(f"✅ Version SVG générée : {svg_output}")
        
        return output_path, svg_output
        
    except Exception as e:
        print(f"❌ Erreur : {e}")
        print("\n💡 Solutions alternatives :")
        print("   1. Installer mermaid-cli : npm install -g @mermaid-js/mermaid-cli")
        print("   2. Puis exécuter : mmdc -i architecture_diagram.mmd -o architecture.png")
        print("   3. Ou utiliser https://mermaid.live (copier-coller le contenu)")
        return None


def afficher_instructions_mermaid_cli():
    """Affiche les instructions pour utiliser mermaid-cli"""
    print("""
╔══════════════════════════════════════════════════════════════════╗
║          GÉNÉRER L'IMAGE AVEC MERMAID-CLI (alternative)          ║
╚══════════════════════════════════════════════════════════════════╝

1️⃣  INSTALLER MERMAID-CLI (nécessite Node.js) :
    npm install -g @mermaid-js/mermaid-cli

2️⃣  GÉNÉRER L'IMAGE PNG :
    mmdc -i architecture_diagram.mmd -o architecture.png -b transparent

3️⃣  GÉNÉRER EN HAUTE RÉSOLUTION :
    mmdc -i architecture_diagram.mmd -o architecture.png -w 2400 -H 1800

4️⃣  GÉNÉRER EN SVG (vectoriel) :
    mmdc -i architecture_diagram.mmd -o architecture.svg

══════════════════════════════════════════════════════════════════

📌 OPTIONS UTILES :
   -b white          → Fond blanc
   -b transparent    → Fond transparent
   -t dark           → Thème sombre
   -w 2400           → Largeur 2400px
   -H 1800           → Hauteur 1800px

══════════════════════════════════════════════════════════════════
""")


if __name__ == "__main__":
    print("╔══════════════════════════════════════════════════════════════════╗")
    print("║         GÉNÉRATEUR D'IMAGE - ARCHITECTURE PROJET EXAMENS         ║")
    print("╚══════════════════════════════════════════════════════════════════╝")
    print()
    
    # Tenter de générer via l'API Mermaid.ink
    result = generer_image_architecture()
    
    print()
    print("─" * 70)
    
    # Afficher les instructions pour mermaid-cli
    afficher_instructions_mermaid_cli()
    
    if result:
        print(f"\n✅ Fichiers générés avec succès !")
        print(f"   📁 PNG : architecture.png")
        print(f"   📁 SVG : architecture.svg")
    else:
        print(f"\n⚠️  Utilisez une des méthodes alternatives ci-dessus")
