# Configuración de GitHub Pages

Este documento explica cómo configurar y publicar la página web en GitHub Pages.

## Pasos para Activar GitHub Pages

### 1. Subir los Cambios a GitHub

Primero, asegúrate de que todos los archivos estén en el repositorio:

```bash
git add docs/index.html docs/styles.css docs/GITHUB_PAGES_SETUP.md
git commit -m "feat: add GitHub Pages with Spanish documentation"
git push origin main
```

### 2. Configurar GitHub Pages desde el Repositorio

1. Ve a tu repositorio en GitHub: https://github.com/pedroid999/test-antigravity
2. Haz clic en **Settings** (Configuración)
3. En el menú lateral, haz clic en **Pages**
4. En la sección **Source** (Fuente):
   - Selecciona la rama: **main**
   - Selecciona la carpeta: **/docs**
   - Haz clic en **Save**

### 3. Esperar el Despliegue

GitHub Pages tardará unos minutos en construir y desplegar el sitio. Una vez completado, verás un mensaje indicando que tu sitio está publicado en:

```
https://pedroid999.github.io/test-antigravity/
```

## Verificar el Sitio

Una vez desplegado, visita la URL para verificar que todo funciona correctamente:
- Las imágenes se cargan correctamente
- Los enlaces funcionan
- El diseño es responsive
- Las animaciones se ejecutan suavemente

## Actualizar el Contenido

Para actualizar el sitio en el futuro:

1. **Edita los archivos** en la carpeta `docs/`:
   - `index.html` - Contenido principal
   - `styles.css` - Estilos y diseño

2. **Commit y push:**
   ```bash
   git add docs/
   git commit -m "docs: update GitHub Pages content"
   git push origin main
   ```

3. **Espera** unos minutos para que GitHub Pages se actualice automáticamente

## Personalización del Dominio (Opcional)

Si tienes un dominio personalizado:

1. En **Settings → Pages**, añade tu dominio en **Custom domain**
2. Configura los registros DNS según las instrucciones de GitHub
3. Habilita **Enforce HTTPS** para seguridad

## Estructura de Archivos

```
docs/
├── index.html              # Página principal
├── styles.css              # Estilos CSS
├── GITHUB_PAGES_SETUP.md   # Esta guía
├── ANTIGRAVITY_CREATION.md # Documentación del proceso
├── walkthrough.md          # Walkthrough del proyecto
└── images/                 # Capturas de pantalla
    ├── full_registration_test_1763887885791.webp
    └── verify_profile_and_logout_1763887984703.webp
```

## Enlaces Útiles

- **Repositorio:** https://github.com/pedroid999/test-antigravity
- **Documentación de GitHub Pages:** https://docs.github.com/en/pages
- **Guía de Custom Domains:** https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site

## Solución de Problemas

### Las imágenes no se cargan
- Verifica que las rutas sean relativas: `images/nombre.webp`
- Asegúrate de que las imágenes estén en la carpeta `docs/images/`

### El CSS no se aplica
- Revisa que `styles.css` esté en la misma carpeta que `index.html`
- Verifica que el `<link>` en el HTML sea correcto

### El sitio no se actualiza
- Los cambios pueden tardar 1-5 minutos en reflejarse
- Limpia la caché del navegador (Ctrl+Shift+R o Cmd+Shift+R)
- Verifica que el commit se haya subido correctamente a GitHub

## Compartir en Redes Sociales

### LinkedIn
Para compartir en LinkedIn, publica tu artículo con:
- **Título:** "Desarrollo Full-Stack con Google Antigravity: Un Caso de Estudio"
- **URL:** https://pedroid999.github.io/test-antigravity/
- **Descripción:** Breve resumen del proyecto y el potencial de desarrollo asistido por IA

### Medium
Si escribes un artículo en Medium:
- Incluye screenshots de la página
- Enlaza al sitio y al repositorio
- Destaca el proceso de desarrollo con Antigravity
- Añade código de ejemplo del repositorio

## Métricas y Analytics (Opcional)

Para añadir Google Analytics u otras herramientas:

1. Obtén tu ID de seguimiento
2. Añade el script antes de `</head>` en `index.html`:
   ```html
   <!-- Google Analytics -->
   <script async src="https://www.googletagmanager.com/gtag/js?id=TU_ID"></script>
   <script>
     window.dataLayer = window.dataLayer || [];
     function gtag(){dataLayer.push(arguments);}
     gtag('js', new Date());
     gtag('config', 'TU_ID');
   </script>
   ```

---

**¡Listo!** Tu GitHub Pages está configurada y lista para impresionar a la comunidad técnica. 🚀
