# Comment générer l'image de l'architecture

## 📋 3 Méthodes possibles

---

## **Méthode 1 : Mermaid Live Editor** ⭐ (RECOMMANDÉ - le plus simple)

### Étapes :
1. **Ouvrir** https://mermaid.live
2. **Copier-coller** le contenu du fichier `architecture_diagram.mmd` dans l'éditeur
3. **Cliquer** sur le bouton **"PNG"** ou **"SVG"** pour télécharger l'image
4. **Résultat** : Image haute qualité avec les couleurs et le style

---

## **Méthode 2 : Extension VS Code Mermaid**

### Installation :
1. Installer l'extension **"Markdown Preview Mermaid Support"** ou **"Mermaid Editor"**
2. Ouvrir le fichier `architecture_diagram.mmd`
3. Clic droit → **"Preview Mermaid"** ou **"Export as PNG/SVG"**

### Extensions recommandées :
- **Mermaid Preview** (bierner.markdown-mermaid)
- **Mermaid Editor** (tomoyukim.vscode-mermaid-editor)

---

## **Méthode 3 : Mermaid CLI** (ligne de commande)

### Installation :
```bash
npm install -g @mermaid-js/mermaid-cli
```

### Générer l'image :
```bash
# PNG
mmdc -i architecture_diagram.mmd -o architecture.png -b transparent

# SVG (vectoriel, meilleure qualité)
mmdc -i architecture_diagram.mmd -o architecture.svg -b transparent

# PNG haute résolution
mmdc -i architecture_diagram.mmd -o architecture.png -w 2400 -H 1800 -b white
```

### Options utiles :
- `-b white` ou `-b transparent` : couleur de fond
- `-w 2400` : largeur en pixels
- `-H 1800` : hauteur en pixels
- `-t dark` : thème sombre

---

## **Méthode 4 : Intégrer dans le document Word** (déjà fait)

Le fichier Word généré (`Architecture_Projet_Examens.docx`) contient déjà le diagramme Mermaid rendu.

---

## 📁 Fichiers générés

- `architecture_diagram.mmd` : Code source Mermaid
- `Architecture_Projet_Examens.docx` : Document Word complet avec tableaux
- `generer_image_architecture.py` : Script Python pour générer l'image automatiquement

---

## 🎨 Personnalisation des couleurs

Dans le fichier `.mmd`, vous pouvez modifier les couleurs :

```mermaid
style FRONTEND fill:#1e3a5f,stroke:#4a90d9,color:#fff
style BACKEND fill:#8b4513,stroke:#d2691e,color:#fff
style DATABASE fill:#2d5016,stroke:#6abf40,color:#fff
style IA fill:#5c1a5c,stroke:#c056c0,color:#fff
```

**Format** : `fill:#RRGGBB` (couleur de fond), `stroke:#RRGGBB` (bordure), `color:#fff` (texte)

---

## 🚀 Résultat attendu

L'image générée affichera :
- **Bleu foncé** : Frontend (React)
- **Marron** : Backend (Node.js)
- **Vert** : Base de données (PostgreSQL)
- **Violet** : IA (FastAPI)
- **Or** : Services externes (Ollama, Transformers)

Les flèches montrent les flux de communication entre les composants.
