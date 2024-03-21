Miembros del equipo:
Rafael Gil 
Mario Calleja
Kutman Eshenkulov






El git se divvide en diferentes partes:

En main se encuentra el web scraping que es de donde se han sacado  "abecedario_es" y "abecedario2" con la libreria "request" de la pagina "https://www.fundacioncnse.org/educa/bancolse/#0&gsc.tab=0".

"Imagenes modelo" hace referendia a las imagenes procesadas en la pagina roboflow donde el resultado ha sido del 12% de precision y dentro del docx adjunto se pueden ver las puntuaciones y en data.yaml se puede ver mas informacion a parte.

"hugging.py" es el modelo que hemos elegido de la web "https://huggingface.co/RavenOnur/Sign-Language" .

"modelo.py" es el modelo elegido pero aplicado a nuestra imagenes scrapeadas.

