# informatorio
Guardar codigo rapido en VSC ===> CTRL + S

Comandos para subir a github nuestro codigo:
- Pre-requisito: Estar parado sobre la carpeta de nuestro repositorio
Como nos damos cuenta de esto? Corro: 

En windows: `ls -force`

En linux: `ls -la`

Y si esta el archivo .git estoy bien

> Supongamos que lo que esta escrito en nuestra carta es nuestro codigo

- Trackeo de archivos: --> Poniendo carta en sobre
    - `git add .` agrego todo lo que esta en `pwd`
    - `git add README.md` agrego solo ese archivo
- Guardar en git localmente: --> Firmando la carta con el destinatario y fecha, etc, etc
    - `git commit -m "MENSAJE DEL CAMBIO"`
- Subir codigo a github:
    - `git push origin main` --> Poniendo el sobre con la carta en el buzon
    --> SE ENVIA A GITHUB

Si les salen problemas deben correr: `git config --global user.email "TU EMAIL"`

Deben loguearse con su cuenta de github


