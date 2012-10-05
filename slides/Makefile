
default: ../index.html

../index.html:
	landslide -i -l no  -r slides.md -d ../index.html

pdf: default
	prince presentation.html -s theme/css/pdf.css -o out.pdf
	
clean:
	-rm ../index.html
