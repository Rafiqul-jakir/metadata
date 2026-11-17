#!/usr/bin/env python3
"""Generates all localized pages + sitemap. Usage: python build.py https://USERNAME.github.io/REPO  (no trailing slash)"""
import sys, json, os
BASE = (sys.argv[1] if len(sys.argv) > 1 else "https://rafiqul-jakir.github.io/metadata").rstrip("/")
EMAIL = "rafiquljakir@gmail.com"
LANGS = ["en", "es", "fr", "it", "de"]
FLAG = {"en": "🇬🇧 English", "es": "🇪🇸 Español", "fr": "🇫🇷 Français", "it": "🇮🇹 Italiano", "de": "🇩🇪 Deutsch"}
# Editable statistics (shown in hero)
STATS = ["300,000+", "", ""]

T = {
"en": dict(
 title="Nature.com Metadata Dataset | Scientific Publication Metadata – ResearchMeta Data",
 kw=['Nature.com metadata dataset', 'Nature scientific papers dataset', 'Nature publication metadata', 'scientific research paper dataset', 'scientific publication metadata', 'research paper metadata database', 'academic publication dataset', 'scholarly metadata dataset', 'DOI dataset', 'research publication database', 'scientific article metadata', 'academic research data', 'author affiliation dataset', 'research bibliometric dataset', 'scientific publication CSV', 'research analytics dataset', 'academic data for machine learning', 'scholarly publication data', 'Springer Nature metadata', 'Scientific Reports metadata', 'buy research paper dataset', 'research paper CSV download', 'journal article metadata dataset', 'bibliometric analysis data', 'author country dataset', 'research keywords dataset', 'scientific papers database download', 'research intelligence data', 'academic search engine dataset', 'DOI and article URL dataset'], desc="Scientific publication metadata dataset: 300,000+ Nature.com / Springer Nature records with DOI, titles, authors, affiliations, countries, keywords. CSV sample.",
 nav=["Home","About Dataset","Data Fields","Sample Data","Packages","FAQ","Contact"], req="Request Dataset",
 h1="Unlock the World's Scientific Research Metadata.",
 lead="Access a large, structured collection of historical scientific publication metadata from Nature.com / Springer Nature. Explore scientific publications through titles, DOIs, authors, affiliations, publication dates, article types, countries, and keywords.",
 c1="Explore Dataset", c2="View Packages", st=["Scientific Records","Historical Publication Metadata","Global Research Coverage"],
 ah="A Structured Scientific Publication Dataset",
 ap="Scientific publications generate enormous amounts of valuable information. Our dataset brings together structured metadata from historical Nature.com / Springer Nature publication records, making it easier for researchers, institutions, developers, and analytical teams to explore and process scholarly publication information.",
 cards=[("Publication Information","Paper titles, DOIs, article URLs, publication dates, article types, journal information."),("Author Intelligence","Author names, co-authorship, affiliations and institutional associations."),("Geographic Information","Author country information, institutional locations where available."),("Research Discovery","Research keywords, publication classification, topic exploration.")],
 uh="Built for Research, Analytics, and Data-Driven Innovation",
 uses=[("Academic Research","Study publication trends and history."),("Bibliometric Analysis","Analyze collaborations, institutions and output by country."),("AI and Machine Learning","Metadata classification and discovery models. Full texts, abstracts or training rights are not included unless separately licensed."),("Research Discovery Platforms","Academic search engines and publication directories."),("Institutional Analytics","Publication analysis and collaboration patterns."),("Commercial Data Applications","Research intelligence products and custom data solutions.")],
 fh="Explore the Available Data Fields", fn="Metadata availability can differ across individual records.",
 sh="Preview the Dataset", ss="Explore the structure and level of detail available in the scientific publication metadata.",
 cols=["Record ID","DOI","Article Title","Journal","Publication Date","Article Type","Authors","Affiliation","Country","Keywords"],
 sd="Preview of 100 records from the dataset. Metadata availability can differ across individual records.",
 ph="Choose Your Research Metadata Package", ps="Flexible dataset packages for researchers, organizations, developers, and commercial data users.",
 recs="scientific publication records", inc="Structured metadata, DOIs, titles and URLs, authors and affiliations, dates and article types, countries and keywords.",
 pop="Popular Choice", pn=["Starter Dataset","Professional Dataset","Enterprise Dataset"], pb=["Request Starter Package","Request Professional Package","Request Enterprise Package"],
 pnote="Final dataset availability, licensing terms, delivery format, and transaction details will be confirmed directly with the customer.",
 kh="Interested in Purchasing the Dataset?", kp="Choose your preferred dataset package and prepare your inquiry. Simply copy the generated email subject and message, then send them to our contact email address.",
 lab=["Full Name","Email Address","Organization (Optional)","Dataset Package","Message"],
 ph_=["Enter your full name","Enter your email address","University, company, research institution, or independent researcher","Tell us about your requirements, intended usage, preferred format, or questions about the dataset."],
 opts=["Starter Dataset — 100,000 Records — $99","Professional Dataset — 200,000 Records — $199","Enterprise Dataset — 300,000 Records — $299","Custom Dataset Inquiry"],
 gen="Generate Email Inquiry", priv="Your information is processed locally in your browser to generate an email inquiry. This website does not submit or store your form information. You must send the generated email yourself.",
 to="To",sub="Subject",msg="Message",cs="Copy Subject",cb="Copy Email Message",ca="Copy Full Email",op="Open Email Application",ok="Copied successfully!",fail="Copy failed. Please select the text and copy it manually.",
 errs=["Please enter your full name.","Please enter a valid email address.","Please choose a package."],
 subj=["Dataset Purchase Inquiry – Starter (100,000 Records)","Dataset Purchase Inquiry – Professional (200,000 Records)","Dataset Purchase Inquiry – Enterprise (300,000 Records)","Dataset Purchase Inquiry – Custom Dataset"],
 body="Dear ResearchMeta Data Team,\n\nI am interested in purchasing your scientific research publication metadata dataset.\n\nMy Details:\n\nFull Name: {name}\nEmail Address: {email}\nOrganization: {org}\nSelected Package: {pkg}\nPackage Price: {price}\n\nMessage:\n\n{msg}\n\nI would appreciate further information regarding dataset availability, licensing terms, delivery format, and purchasing procedures.\n\nThank you for your time.\n\nBest regards,\n{name}",
 dm="I would like to receive more information about this dataset package, including sample data, delivery format, licensing terms, and the purchasing procedure.", dl="Download Demo Data (CSV)", none="Not provided", custom="Custom quote",
 disc="This is an independently offered scientific publication metadata dataset. It is not an official Nature.com or Springer Nature product and is not affiliated with, endorsed by, or sponsored by Springer Nature.",
 fl="Structured scientific publication metadata for research, discovery, and analytics.",
 fd="ResearchMeta Data is an independent dataset offering. It is not affiliated with, sponsored by, or endorsed by Springer Nature or Nature.com. All trademarks belong to their respective owners.",
 lic="Usage and redistribution rights depend on the applicable licence and the commercial terms agreed with the buyer. Licensing terms are confirmed during the inquiry.",
 fq=[("Is this an official Nature.com dataset?","No. It is an independently offered metadata dataset, not affiliated with Springer Nature."),("What delivery formats are available?","The preferred format can be discussed during the inquiry."),("How can I purchase a package?","Choose a package, generate the email inquiry in the contact section, and send it yourself from your email application. Nothing is sent automatically."),("Can I use the metadata for AI and machine learning?","Metadata can support classification and discovery experiments. Rights depend on the licence agreed commercially.")], faq="Frequently Asked Questions"),
"es": dict(
 title="Dataset de metadatos de Nature.com | Metadatos de publicaciones científicas – ResearchMeta Data",
 kw=['dataset de metadatos de Nature.com', 'base de datos de artículos científicos de Nature', 'metadatos de publicaciones científicas', 'dataset de artículos de investigación', 'base de datos de metadatos de artículos científicos', 'dataset de publicaciones académicas', 'metadatos académicos', 'dataset de DOI', 'base de datos de publicaciones científicas', 'datos de investigación académica', 'dataset de afiliaciones de autores', 'dataset bibliométrico', 'publicaciones científicas CSV', 'dataset de analítica de investigación', 'datos académicos para aprendizaje automático', 'metadatos de Springer Nature', 'comprar dataset de artículos científicos', 'descargar metadatos de artículos en CSV', 'análisis bibliométrico datos', 'palabras clave de investigación dataset', 'datos para motores de búsqueda académicos'], desc="Dataset de metadatos de publicaciones científicas: más de 300.000 registros de Nature.com / Springer Nature con DOI, títulos, autores, afiliaciones y países. Muestra CSV.",
 nav=["Inicio","Sobre el dataset","Campos de datos","Muestra","Paquetes","Preguntas frecuentes","Contacto"], req="Solicitar dataset",
 h1="Descubra los metadatos de la investigación científica mundial.",
 lead="Acceda a una amplia colección estructurada de metadatos históricos de publicaciones científicas de Nature.com / Springer Nature: títulos, DOI, autores, afiliaciones, fechas de publicación, tipos de artículo, países y palabras clave.",
 c1="Explorar dataset", c2="Ver paquetes", st=["Registros científicos","Metadatos históricos de publicaciones","Cobertura de investigación global"],
 ah="Un dataset estructurado de publicaciones científicas",
 ap="Las publicaciones científicas generan enormes cantidades de información valiosa. Nuestro dataset reúne metadatos estructurados de registros históricos de Nature.com / Springer Nature para que investigadores, instituciones, desarrolladores y equipos analíticos exploren y procesen información bibliográfica.",
 cards=[("Información de publicaciones","Títulos, DOI, URL de artículos, fechas de publicación, tipos de artículo y revista."),("Inteligencia de autores","Nombres de autores, coautoría, afiliaciones y asociaciones institucionales."),("Información geográfica","País de los autores y ubicación institucional cuando esté disponible."),("Descubrimiento científico","Palabras clave, clasificación de publicaciones y exploración de temas.")],
 uh="Creado para la investigación, el análisis y la innovación basada en datos",
 uses=[("Investigación académica","Estudie tendencias e historia de las publicaciones."),("Análisis bibliométrico","Analice colaboraciones, instituciones y producción por país."),("IA y aprendizaje automático","Clasificación de metadatos y modelos de descubrimiento. No incluye textos completos, resúmenes ni derechos de entrenamiento salvo licencia aparte."),("Plataformas de descubrimiento","Buscadores académicos y directorios de publicaciones."),("Análisis institucional","Análisis de publicaciones y patrones de colaboración."),("Aplicaciones comerciales","Productos de inteligencia de investigación y soluciones a medida.")],
 fh="Explore los campos de datos disponibles", fn="La disponibilidad de metadatos puede variar entre registros.",
 sh="Vista previa del dataset", ss="Explore la estructura y el nivel de detalle de los metadatos de publicaciones científicas.",
 cols=["ID de registro","DOI","Título del artículo","Revista","Fecha de publicación","Tipo de artículo","Autores","Afiliación","País","Palabras clave"],
 sd="Vista previa de 100 registros del dataset. La disponibilidad de metadatos puede variar entre registros.",
 ph="Elija su paquete de metadatos", ps="Paquetes flexibles para investigadores, organizaciones, desarrolladores y usuarios comerciales.",
 recs="registros de publicaciones científicas", inc="Metadatos estructurados, DOI, títulos y URL, autores y afiliaciones, fechas y tipos de artículo, países y palabras clave.",
 pop="Opción popular", pn=["Dataset Starter","Dataset Professional","Dataset Enterprise"], pb=["Solicitar paquete Starter","Solicitar paquete Professional","Solicitar paquete Enterprise"],
 pnote="La disponibilidad final, los términos de licencia, el formato de entrega y los detalles de la transacción se confirmarán directamente con el cliente.",
 kh="¿Le interesa comprar el dataset?", kp="Elija su paquete y prepare su consulta. Copie el asunto y el mensaje generados y envíelos a nuestra dirección de correo.",
 lab=["Nombre completo","Correo electrónico","Organización (opcional)","Paquete de datos","Mensaje"],
 ph_=["Introduzca su nombre completo","Introduzca su correo electrónico","Universidad, empresa, institución o investigador independiente","Cuéntenos sus requisitos, uso previsto, formato preferido o dudas sobre el dataset."],
 opts=["Dataset Starter — 100.000 registros — $99","Dataset Professional — 200.000 registros — $199","Dataset Enterprise — 300.000 registros — $299","Consulta de dataset personalizado"],
 gen="Generar consulta por correo", priv="Su información se procesa localmente en su navegador para generar la consulta. Este sitio no envía ni almacena los datos del formulario. Usted debe enviar el correo generado.",
 to="Para",sub="Asunto",msg="Mensaje",cs="Copiar asunto",cb="Copiar mensaje",ca="Copiar correo completo",op="Abrir aplicación de correo",ok="¡Copiado correctamente!",fail="No se pudo copiar. Seleccione el texto y cópielo manualmente.",
 errs=["Introduzca su nombre completo.","Introduzca un correo electrónico válido.","Elija un paquete."],
 subj=["Consulta de compra de dataset – Starter (100.000 registros)","Consulta de compra de dataset – Professional (200.000 registros)","Consulta de compra de dataset – Enterprise (300.000 registros)","Consulta de compra de dataset – Dataset personalizado"],
 body="Estimado equipo de ResearchMeta Data:\n\nMe interesa adquirir su dataset de metadatos de publicaciones científicas.\n\nMis datos:\n\nNombre completo: {name}\nCorreo electrónico: {email}\nOrganización: {org}\nPaquete seleccionado: {pkg}\nPrecio del paquete: {price}\n\nMensaje:\n\n{msg}\n\nAgradecería más información sobre disponibilidad, términos de licencia, formato de entrega y procedimiento de compra.\n\nGracias por su tiempo.\n\nAtentamente,\n{name}",
 dm="Me gustaría recibir más información sobre este paquete de datos, incluidos datos de muestra, formato de entrega, términos de licencia y procedimiento de compra.", dl="Descargar datos de muestra (CSV)", none="No indicado", custom="Presupuesto a medida",
 disc="Este es un dataset de metadatos de publicaciones científicas ofrecido de forma independiente. No es un producto oficial de Nature.com ni de Springer Nature y no está afiliado, respaldado ni patrocinado por Springer Nature.",
 fl="Metadatos estructurados de publicaciones científicas para investigación, descubrimiento y análisis.",
 fd="ResearchMeta Data es una oferta de datos independiente. No está afiliada, patrocinada ni respaldada por Springer Nature o Nature.com. Todas las marcas pertenecen a sus respectivos propietarios.",
 lic="Los derechos de uso y redistribución dependen de la licencia aplicable y de los términos comerciales acordados con el comprador.",
 fq=[("¿Es un dataset oficial de Nature.com?","No. Es un dataset de metadatos ofrecido de forma independiente, sin afiliación con Springer Nature."),("¿Qué formatos de entrega hay?","El formato preferido puede acordarse durante la consulta."),("¿Cómo compro un paquete?","Elija un paquete, genere la consulta en la sección de contacto y envíela usted mismo desde su aplicación de correo. No se envía nada automáticamente."),("¿Puedo usar los metadatos para IA?","Pueden servir para experimentos de clasificación y descubrimiento. Los derechos dependen de la licencia acordada.")], faq="Preguntas frecuentes"),
"fr": dict(
 title="Jeu de données de métadonnées Nature.com | Métadonnées de publications scientifiques – ResearchMeta Data",
 kw=['jeu de données de métadonnées Nature.com', "base de données d'articles scientifiques Nature", 'métadonnées de publications scientifiques', "jeu de données d'articles de recherche", "base de métadonnées d'articles scientifiques", 'jeu de données de publications académiques', 'métadonnées académiques', 'jeu de données DOI', 'base de données de publications de recherche', 'données de recherche académique', "jeu de données d'affiliations d'auteurs", 'jeu de données bibliométrique', 'publications scientifiques CSV', "jeu de données d'analyse de la recherche", "données académiques pour l'apprentissage automatique", 'métadonnées Springer Nature', "acheter un jeu de données d'articles scientifiques", "télécharger métadonnées d'articles CSV", "données d'analyse bibliométrique", 'mots-clés de recherche jeu de données', 'données pour moteur de recherche académique'], desc="Jeu de données de métadonnées scientifiques : plus de 300 000 enregistrements Nature.com / Springer Nature avec DOI, titres, auteurs, affiliations, pays. Échantillon CSV.",
 nav=["Accueil","À propos","Champs de données","Échantillon","Offres","FAQ","Contact"], req="Demander le jeu de données",
 h1="Accédez aux métadonnées de la recherche scientifique mondiale.",
 lead="Accédez à une vaste collection structurée de métadonnées historiques de publications scientifiques de Nature.com / Springer Nature : titres, DOI, auteurs, affiliations, dates de publication, types d'articles, pays et mots-clés.",
 c1="Explorer le jeu de données", c2="Voir les offres", st=["Enregistrements scientifiques","Métadonnées historiques de publications","Couverture mondiale de la recherche"],
 ah="Un jeu de données structuré de publications scientifiques",
 ap="Les publications scientifiques produisent d'énormes quantités d'informations précieuses. Notre jeu de données rassemble des métadonnées structurées issues d'enregistrements historiques de Nature.com / Springer Nature pour aider chercheurs, institutions, développeurs et équipes d'analyse à explorer l'information scientifique.",
 cards=[("Informations sur les publications","Titres, DOI, URL d'articles, dates de publication, types d'articles, revue."),("Intelligence des auteurs","Noms des auteurs, co-signatures, affiliations et rattachements institutionnels."),("Informations géographiques","Pays des auteurs et localisation des institutions lorsque disponible."),("Découverte scientifique","Mots-clés, classification des publications et exploration des sujets.")],
 uh="Conçu pour la recherche, l'analyse et l'innovation fondée sur les données",
 uses=[("Recherche académique","Étudiez les tendances et l'histoire des publications."),("Analyse bibliométrique","Analysez collaborations, institutions et production par pays."),("IA et apprentissage automatique","Classification de métadonnées et modèles de découverte. Textes intégraux, résumés et droits d'entraînement non inclus sauf licence distincte."),("Plateformes de découverte","Moteurs de recherche académiques et annuaires de publications."),("Analyse institutionnelle","Analyse des publications et des collaborations."),("Applications commerciales","Produits d'intelligence de recherche et solutions sur mesure.")],
 fh="Découvrez les champs de données disponibles", fn="La disponibilité des métadonnées peut varier selon les enregistrements.",
 sh="Aperçu du jeu de données", ss="Découvrez la structure et le niveau de détail des métadonnées de publications scientifiques.",
 cols=["ID","DOI","Titre de l'article","Revue","Date de publication","Type d'article","Auteurs","Affiliation","Pays","Mots-clés"],
 sd="Aperçu de 100 enregistrements du jeu de données. La disponibilité des métadonnées peut varier selon les enregistrements.",
 ph="Choisissez votre offre de métadonnées", ps="Des offres flexibles pour chercheurs, organisations, développeurs et utilisateurs commerciaux.",
 recs="enregistrements de publications scientifiques", inc="Métadonnées structurées, DOI, titres et URL, auteurs et affiliations, dates et types d'articles, pays et mots-clés.",
 pop="Choix populaire", pn=["Jeu Starter","Jeu Professional","Jeu Enterprise"], pb=["Demander l'offre Starter","Demander l'offre Professional","Demander l'offre Enterprise"],
 pnote="La disponibilité finale, les conditions de licence, le format de livraison et les détails de la transaction seront confirmés directement avec le client.",
 kh="Intéressé par l'achat du jeu de données ?", kp="Choisissez votre offre et préparez votre demande. Copiez l'objet et le message générés, puis envoyez-les à notre adresse e-mail.",
 lab=["Nom complet","Adresse e-mail","Organisation (facultatif)","Offre de données","Message"],
 ph_=["Saisissez votre nom complet","Saisissez votre adresse e-mail","Université, entreprise, institution ou chercheur indépendant","Décrivez vos besoins, l'usage prévu, le format souhaité ou vos questions."],
 opts=["Jeu Starter — 100 000 enregistrements — 99 $","Jeu Professional — 200 000 enregistrements — 199 $","Jeu Enterprise — 300 000 enregistrements — 299 $","Demande de jeu personnalisé"],
 gen="Générer la demande par e-mail", priv="Vos informations sont traitées localement dans votre navigateur pour générer la demande. Ce site ne transmet ni ne stocke vos données. Vous devez envoyer vous-même l'e-mail généré.",
 to="À",sub="Objet",msg="Message",cs="Copier l'objet",cb="Copier le message",ca="Copier l'e-mail complet",op="Ouvrir l'application e-mail",ok="Copié avec succès !",fail="Échec de la copie. Sélectionnez le texte et copiez-le manuellement.",
 errs=["Veuillez saisir votre nom complet.","Veuillez saisir une adresse e-mail valide.","Veuillez choisir une offre."],
 subj=["Demande d'achat de jeu de données – Starter (100 000 enregistrements)","Demande d'achat de jeu de données – Professional (200 000 enregistrements)","Demande d'achat de jeu de données – Enterprise (300 000 enregistrements)","Demande d'achat de jeu de données – Jeu personnalisé"],
 body="Bonjour l'équipe ResearchMeta Data,\n\nJe souhaite acquérir votre jeu de données de métadonnées de publications scientifiques.\n\nMes coordonnées :\n\nNom complet : {name}\nAdresse e-mail : {email}\nOrganisation : {org}\nOffre choisie : {pkg}\nPrix : {price}\n\nMessage :\n\n{msg}\n\nJe vous remercie de m'indiquer la disponibilité, les conditions de licence, le format de livraison et la procédure d'achat.\n\nMerci de votre temps.\n\nCordialement,\n{name}",
 dm="Je souhaite recevoir plus d'informations sur cette offre, notamment des données d'exemple, le format de livraison, les conditions de licence et la procédure d'achat.", dl="Télécharger les données de démonstration (CSV)", none="Non renseigné", custom="Devis sur mesure",
 disc="Ce jeu de métadonnées de publications scientifiques est proposé de manière indépendante. Ce n'est pas un produit officiel de Nature.com ou de Springer Nature et il n'est ni affilié, ni approuvé, ni parrainé par Springer Nature.",
 fl="Métadonnées structurées de publications scientifiques pour la recherche, la découverte et l'analyse.",
 fd="ResearchMeta Data est une offre de données indépendante, non affiliée, parrainée ou approuvée par Springer Nature ou Nature.com. Toutes les marques appartiennent à leurs propriétaires respectifs.",
 lic="Les droits d'utilisation et de redistribution dépendent de la licence applicable et des conditions commerciales convenues avec l'acheteur.",
 fq=[("S'agit-il d'un jeu de données officiel de Nature.com ?","Non. C'est un jeu de métadonnées proposé de façon indépendante, sans affiliation avec Springer Nature."),("Quels formats de livraison ?","Le format souhaité peut être discuté lors de la demande."),("Comment acheter une offre ?","Choisissez une offre, générez la demande dans la section contact et envoyez-la vous-même depuis votre application e-mail. Rien n'est envoyé automatiquement."),("Puis-je l'utiliser pour l'IA ?","Les métadonnées peuvent servir à des expériences de classification et de découverte. Les droits dépendent de la licence convenue.")], faq="Questions fréquentes"),
"it": dict(
 title="Dataset di metadati Nature.com | Metadati di pubblicazioni scientifiche – ResearchMeta Data",
 kw=['dataset di metadati Nature.com', 'database di articoli scientifici Nature', 'metadati di pubblicazioni scientifiche', 'dataset di articoli di ricerca', 'database di metadati di articoli scientifici', 'dataset di pubblicazioni accademiche', 'metadati accademici', 'dataset DOI', 'database di pubblicazioni di ricerca', 'dati di ricerca accademica', 'dataset di affiliazioni degli autori', 'dataset bibliometrico', 'pubblicazioni scientifiche CSV', 'dataset per analisi della ricerca', 'dati accademici per machine learning', 'metadati Springer Nature', 'acquistare dataset di articoli scientifici', 'scaricare metadati di articoli CSV', 'dati per analisi bibliometrica', 'parole chiave di ricerca dataset', 'dati per motori di ricerca accademici'], desc="Dataset di metadati di pubblicazioni scientifiche: oltre 300.000 record Nature.com / Springer Nature con DOI, titoli, autori, affiliazioni, paesi. Anteprima CSV.",
 nav=["Home","Il dataset","Campi dati","Anteprima","Pacchetti","FAQ","Contatti"], req="Richiedi il dataset",
 h1="Scopri i metadati della ricerca scientifica mondiale.",
 lead="Accedi a un'ampia raccolta strutturata di metadati storici di pubblicazioni scientifiche di Nature.com / Springer Nature: titoli, DOI, autori, affiliazioni, date di pubblicazione, tipi di articolo, paesi e parole chiave.",
 c1="Esplora il dataset", c2="Vedi i pacchetti", st=["Record scientifici","Metadati storici di pubblicazioni","Copertura globale della ricerca"],
 ah="Un dataset strutturato di pubblicazioni scientifiche",
 ap="Le pubblicazioni scientifiche generano enormi quantità di informazioni preziose. Il nostro dataset riunisce metadati strutturati da record storici di Nature.com / Springer Nature, per aiutare ricercatori, istituzioni, sviluppatori e team analitici a esplorare e trattare le informazioni bibliografiche.",
 cards=[("Informazioni sulle pubblicazioni","Titoli, DOI, URL degli articoli, date di pubblicazione, tipi di articolo, rivista."),("Intelligence sugli autori","Nomi degli autori, coautorialità, affiliazioni e legami istituzionali."),("Informazioni geografiche","Paese degli autori e sede istituzionale, ove disponibile."),("Scoperta scientifica","Parole chiave, classificazione delle pubblicazioni ed esplorazione dei temi.")],
 uh="Pensato per ricerca, analisi e innovazione basata sui dati",
 uses=[("Ricerca accademica","Studia tendenze e storia delle pubblicazioni."),("Analisi bibliometrica","Analizza collaborazioni, istituzioni e produzione per paese."),("IA e machine learning","Classificazione dei metadati e modelli di scoperta. Testi integrali, abstract e diritti di addestramento non inclusi salvo licenza separata."),("Piattaforme di scoperta","Motori di ricerca accademici e directory di pubblicazioni."),("Analisi istituzionale","Analisi delle pubblicazioni e delle collaborazioni."),("Applicazioni commerciali","Prodotti di research intelligence e soluzioni su misura.")],
 fh="Esplora i campi dati disponibili", fn="La disponibilità dei metadati può variare da record a record.",
 sh="Anteprima del dataset", ss="Scopri la struttura e il livello di dettaglio dei metadati delle pubblicazioni scientifiche.",
 cols=["ID record","DOI","Titolo dell'articolo","Rivista","Data di pubblicazione","Tipo di articolo","Autori","Affiliazione","Paese","Parole chiave"],
 sd="Anteprima di 100 record del dataset. La disponibilità dei metadati può variare da record a record.",
 ph="Scegli il tuo pacchetto di metadati", ps="Pacchetti flessibili per ricercatori, organizzazioni, sviluppatori e utenti commerciali.",
 recs="record di pubblicazioni scientifiche", inc="Metadati strutturati, DOI, titoli e URL, autori e affiliazioni, date e tipi di articolo, paesi e parole chiave.",
 pop="Scelta popolare", pn=["Dataset Starter","Dataset Professional","Dataset Enterprise"], pb=["Richiedi il pacchetto Starter","Richiedi il pacchetto Professional","Richiedi il pacchetto Enterprise"],
 pnote="Disponibilità finale, termini di licenza, formato di consegna e dettagli della transazione saranno confermati direttamente con il cliente.",
 kh="Vuoi acquistare il dataset?", kp="Scegli il pacchetto e prepara la richiesta. Copia l'oggetto e il messaggio generati e inviali al nostro indirizzo e-mail.",
 lab=["Nome completo","Indirizzo e-mail","Organizzazione (facoltativo)","Pacchetto dati","Messaggio"],
 ph_=["Inserisci il tuo nome completo","Inserisci il tuo indirizzo e-mail","Università, azienda, istituto o ricercatore indipendente","Descrivi le tue esigenze, l'uso previsto, il formato preferito o le tue domande."],
 opts=["Dataset Starter — 100.000 record — $99","Dataset Professional — 200.000 record — $199","Dataset Enterprise — 300.000 record — $299","Richiesta di dataset personalizzato"],
 gen="Genera la richiesta e-mail", priv="Le tue informazioni sono elaborate localmente nel browser per generare la richiesta. Questo sito non invia né memorizza i dati del modulo. Devi inviare tu stesso l'e-mail generata.",
 to="A",sub="Oggetto",msg="Messaggio",cs="Copia oggetto",cb="Copia messaggio",ca="Copia e-mail completa",op="Apri l'app di posta",ok="Copiato con successo!",fail="Copia non riuscita. Seleziona il testo e copialo manualmente.",
 errs=["Inserisci il tuo nome completo.","Inserisci un indirizzo e-mail valido.","Scegli un pacchetto."],
 subj=["Richiesta di acquisto dataset – Starter (100.000 record)","Richiesta di acquisto dataset – Professional (200.000 record)","Richiesta di acquisto dataset – Enterprise (300.000 record)","Richiesta di acquisto dataset – Dataset personalizzato"],
 body="Gentile team di ResearchMeta Data,\n\nsono interessato ad acquistare il vostro dataset di metadati di pubblicazioni scientifiche.\n\nI miei dati:\n\nNome completo: {name}\nIndirizzo e-mail: {email}\nOrganizzazione: {org}\nPacchetto scelto: {pkg}\nPrezzo del pacchetto: {price}\n\nMessaggio:\n\n{msg}\n\nVi sarei grato di ricevere informazioni su disponibilità, termini di licenza, formato di consegna e procedura di acquisto.\n\nGrazie per il tempo dedicato.\n\nCordiali saluti,\n{name}",
 dm="Vorrei ricevere maggiori informazioni su questo pacchetto, inclusi dati di esempio, formato di consegna, termini di licenza e procedura di acquisto.", dl="Scarica i dati dimostrativi (CSV)", none="Non indicato", custom="Preventivo personalizzato",
 disc="Questo è un dataset di metadati di pubblicazioni scientifiche offerto in modo indipendente. Non è un prodotto ufficiale di Nature.com o Springer Nature e non è affiliato, approvato né sponsorizzato da Springer Nature.",
 fl="Metadati strutturati di pubblicazioni scientifiche per ricerca, scoperta e analisi.",
 fd="ResearchMeta Data è un'offerta di dati indipendente, non affiliata, sponsorizzata o approvata da Springer Nature o Nature.com. Tutti i marchi appartengono ai rispettivi proprietari.",
 lic="I diritti di utilizzo e ridistribuzione dipendono dalla licenza applicabile e dai termini commerciali concordati con l'acquirente.",
 fq=[("È un dataset ufficiale di Nature.com?","No. È un dataset di metadati offerto in modo indipendente, senza affiliazione con Springer Nature."),("Quali formati di consegna?","Il formato preferito può essere discusso durante la richiesta."),("Come acquisto un pacchetto?","Scegli un pacchetto, genera la richiesta nella sezione contatti e inviala tu dal tuo programma di posta. Nulla viene inviato automaticamente."),("Posso usarlo per l'IA?","I metadati possono supportare esperimenti di classificazione e scoperta. I diritti dipendono dalla licenza concordata.")], faq="Domande frequenti"),
"de": dict(
 title="Nature.com-Metadatensatz | Metadaten wissenschaftlicher Publikationen – ResearchMeta Data",
 kw=['Nature.com-Metadatensatz', 'Datenbank wissenschaftlicher Nature-Artikel', 'Metadaten wissenschaftlicher Publikationen', 'Datensatz Forschungsartikel', 'Metadatenbank wissenschaftlicher Artikel', 'Datensatz akademischer Publikationen', 'wissenschaftliche Metadaten', 'DOI-Datensatz', 'Forschungspublikationen Datenbank', 'akademische Forschungsdaten', 'Datensatz Autorenaffiliationen', 'bibliometrischer Datensatz', 'wissenschaftliche Publikationen CSV', 'Datensatz für Forschungsanalytik', 'akademische Daten für maschinelles Lernen', 'Springer-Nature-Metadaten', 'Datensatz wissenschaftlicher Artikel kaufen', 'Artikel-Metadaten CSV herunterladen', 'Daten für bibliometrische Analyse', 'Forschungsschlagwörter Datensatz', 'Daten für akademische Suchmaschinen'], desc="Datensatz mit Metadaten wissenschaftlicher Publikationen: über 300.000 Einträge von Nature.com / Springer Nature mit DOI, Titeln, Autoren, Affiliationen, Ländern. CSV-Beispiel.",
 nav=["Start","Über den Datensatz","Datenfelder","Beispieldaten","Pakete","FAQ","Kontakt"], req="Datensatz anfragen",
 h1="Erschließen Sie die Metadaten der weltweiten Forschung.",
 lead="Greifen Sie auf eine große, strukturierte Sammlung historischer Metadaten wissenschaftlicher Publikationen von Nature.com / Springer Nature zu: Titel, DOI, Autoren, Affiliationen, Veröffentlichungsdaten, Artikeltypen, Länder und Schlagwörter.",
 c1="Datensatz erkunden", c2="Pakete ansehen", st=["Wissenschaftliche Datensätze","Historische Publikationsmetadaten","Globale Forschungsabdeckung"],
 ah="Ein strukturierter Datensatz wissenschaftlicher Publikationen",
 ap="Wissenschaftliche Publikationen erzeugen enorme Mengen wertvoller Informationen. Unser Datensatz bündelt strukturierte Metadaten aus historischen Nature.com-/Springer-Nature-Einträgen, damit Forschende, Institutionen, Entwickler und Analyseteams bibliografische Informationen leichter erkunden und verarbeiten können.",
 cards=[("Publikationsinformationen","Titel, DOI, Artikel-URLs, Veröffentlichungsdaten, Artikeltypen, Zeitschrift."),("Autoreninformationen","Autorennamen, Koautorschaft, Affiliationen und institutionelle Zuordnungen."),("Geografische Informationen","Länder der Autoren und Standorte der Institutionen, sofern verfügbar."),("Forschungsentdeckung","Schlagwörter, Klassifikation von Publikationen und Themenerkundung.")],
 uh="Für Forschung, Analyse und datengetriebene Innovation",
 uses=[("Akademische Forschung","Publikationstrends und -geschichte untersuchen."),("Bibliometrische Analyse","Kooperationen, Institutionen und Output nach Land analysieren."),("KI und maschinelles Lernen","Metadatenklassifikation und Discovery-Modelle. Volltexte, Abstracts oder Trainingsrechte sind nur bei gesonderter Lizenz enthalten."),("Discovery-Plattformen","Akademische Suchmaschinen und Publikationsverzeichnisse."),("Institutionelle Analysen","Publikationsanalysen und Kooperationsmuster."),("Kommerzielle Anwendungen","Research-Intelligence-Produkte und individuelle Datenlösungen.")],
 fh="Die verfügbaren Datenfelder im Überblick", fn="Die Verfügbarkeit der Metadaten kann je Datensatz variieren.",
 sh="Vorschau des Datensatzes", ss="Entdecken Sie Struktur und Detailgrad der Metadaten wissenschaftlicher Publikationen.",
 cols=["Datensatz-ID","DOI","Artikeltitel","Zeitschrift","Veröffentlichungsdatum","Artikeltyp","Autoren","Affiliation","Land","Schlagwörter"],
 sd="Vorschau von 100 Datensätzen aus dem Datensatz. Die Verfügbarkeit der Metadaten kann je Datensatz variieren.",
 ph="Wählen Sie Ihr Metadatenpaket", ps="Flexible Pakete für Forschende, Organisationen, Entwickler und kommerzielle Nutzer.",
 recs="wissenschaftliche Publikationsdatensätze", inc="Strukturierte Metadaten, DOI, Titel und URLs, Autoren und Affiliationen, Daten und Artikeltypen, Länder und Schlagwörter.",
 pop="Beliebteste Wahl", pn=["Starter-Datensatz","Professional-Datensatz","Enterprise-Datensatz"], pb=["Starter-Paket anfragen","Professional-Paket anfragen","Enterprise-Paket anfragen"],
 pnote="Endgültige Verfügbarkeit, Lizenzbedingungen, Lieferformat und Transaktionsdetails werden direkt mit dem Kunden bestätigt.",
 kh="Interesse am Kauf des Datensatzes?", kp="Wählen Sie Ihr Paket und bereiten Sie Ihre Anfrage vor. Kopieren Sie Betreff und Nachricht und senden Sie sie an unsere E-Mail-Adresse.",
 lab=["Vollständiger Name","E-Mail-Adresse","Organisation (optional)","Datenpaket","Nachricht"],
 ph_=["Geben Sie Ihren vollständigen Namen ein","Geben Sie Ihre E-Mail-Adresse ein","Universität, Unternehmen, Forschungseinrichtung oder unabhängige Forschung","Beschreiben Sie Ihre Anforderungen, den Verwendungszweck, das gewünschte Format oder Ihre Fragen."],
 opts=["Starter-Datensatz — 100.000 Datensätze — 99 $","Professional-Datensatz — 200.000 Datensätze — 199 $","Enterprise-Datensatz — 300.000 Datensätze — 299 $","Anfrage für individuellen Datensatz"],
 gen="E-Mail-Anfrage erstellen", priv="Ihre Angaben werden lokal in Ihrem Browser verarbeitet, um eine E-Mail-Anfrage zu erstellen. Diese Website übermittelt oder speichert keine Formulardaten. Sie müssen die erstellte E-Mail selbst senden.",
 to="An",sub="Betreff",msg="Nachricht",cs="Betreff kopieren",cb="Nachricht kopieren",ca="Gesamte E-Mail kopieren",op="E-Mail-Programm öffnen",ok="Erfolgreich kopiert!",fail="Kopieren fehlgeschlagen. Markieren Sie den Text und kopieren Sie ihn manuell.",
 errs=["Bitte geben Sie Ihren vollständigen Namen ein.","Bitte geben Sie eine gültige E-Mail-Adresse ein.","Bitte wählen Sie ein Paket."],
 subj=["Kaufanfrage Datensatz – Starter (100.000 Datensätze)","Kaufanfrage Datensatz – Professional (200.000 Datensätze)","Kaufanfrage Datensatz – Enterprise (300.000 Datensätze)","Kaufanfrage Datensatz – Individueller Datensatz"],
 body="Sehr geehrtes ResearchMeta-Data-Team,\n\nich interessiere mich für den Kauf Ihres Datensatzes mit Metadaten wissenschaftlicher Publikationen.\n\nMeine Angaben:\n\nVollständiger Name: {name}\nE-Mail-Adresse: {email}\nOrganisation: {org}\nGewähltes Paket: {pkg}\nPaketpreis: {price}\n\nNachricht:\n\n{msg}\n\nIch bitte um weitere Informationen zu Verfügbarkeit, Lizenzbedingungen, Lieferformat und Kaufablauf.\n\nVielen Dank für Ihre Zeit.\n\nMit freundlichen Grüßen\n{name}",
 dm="Ich möchte weitere Informationen zu diesem Datenpaket erhalten, einschließlich Beispieldaten, Lieferformat, Lizenzbedingungen und Kaufablauf.", dl="Beispieldaten herunterladen (CSV)", none="Keine Angabe", custom="Individuelles Angebot",
 disc="Dies ist ein unabhängig angebotener Datensatz mit Metadaten wissenschaftlicher Publikationen. Er ist kein offizielles Produkt von Nature.com oder Springer Nature und steht in keiner Verbindung zu Springer Nature und wird weder von diesem unterstützt noch gesponsert.",
 fl="Strukturierte Metadaten wissenschaftlicher Publikationen für Forschung, Discovery und Analyse.",
 fd="ResearchMeta Data ist ein unabhängiges Datenangebot. Es ist nicht mit Springer Nature oder Nature.com verbunden, wird nicht von diesen gesponsert oder unterstützt. Alle Marken gehören ihren jeweiligen Inhabern.",
 lic="Nutzungs- und Weitergaberechte hängen von der anwendbaren Lizenz und den mit dem Käufer vereinbarten kommerziellen Bedingungen ab.",
 fq=[("Ist dies ein offizieller Nature.com-Datensatz?","Nein. Es ist ein unabhängig angebotener Metadatensatz ohne Verbindung zu Springer Nature."),("Welche Lieferformate gibt es?","Das gewünschte Format kann während der Anfrage besprochen werden."),("Wie kaufe ich ein Paket?","Wählen Sie ein Paket, erstellen Sie die Anfrage im Kontaktbereich und senden Sie sie selbst aus Ihrem E-Mail-Programm. Es wird nichts automatisch gesendet."),("Kann ich die Metadaten für KI nutzen?","Die Metadaten können Klassifikations- und Discovery-Experimente unterstützen. Die Rechte hängen von der vereinbarten Lizenz ab.")], faq="Häufig gestellte Fragen"),
}
HL = {"en":"en","es":"es","fr":"fr","it":"it","de":"de"}
FIELDS = [("DOI","id"),("Article Title","text"),("Article URL","link"),("Journal","text"),("Article Type","text"),("Publication Date","date"),("Received Date","date"),("Accepted Date","date"),("Authors","people"),("Affiliations","people"),("Country","geo"),("Keywords","text")]
PRICES = ["$99","$199","$299"]; RECS = ["100,000","200,000","300,000"]

def esc(s): return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;").replace('"',"&quot;")
def url(l): return BASE + ("/" if l == "en" else f"/{l}/")

def page(l):
    t = T[l]; pre = "" if l == "en" else "../"
    ids = ["home","about","fields","sample","packages","faq","contact"]
    nav = "".join(f'<a href="#{ids[k]}">{esc(t["nav"][k])}</a>' for k in [0,3,1,2,4,5,6])
    alts = "".join(f'<link rel="alternate" hreflang="{x}" href="{url(x)}">' for x in LANGS) + f'<link rel="alternate" hreflang="x-default" href="{url("en")}">'
    opts = "".join(f'<option value="{v}">{esc(o)}</option>' for v, o in zip("spec", t["opts"]))
    langs = "".join(f'<option value="{pre}{"" if x=="en" else x+"/"}"{" selected" if x==l else ""} data-l="{x}">{FLAG[x]}</option>' for x in LANGS)
    stats = f'<div><b>{STATS[0]}</b><span>{esc(t["st"][0])}</span></div>' + "".join(f'<div><b>★</b><span>{esc(s)}</span></div>' for s in t["st"][1:])
    cards = "".join(f'<article class="card"><h3>{esc(a)}</h3><p>{esc(b)}</p></article>' for a, b in t["cards"])
    uses = "".join(f'<article class="card"><h3>{esc(a)}</h3><p>{esc(b)}</p></article>' for a, b in t["uses"])
    fields = "".join(f'<li class="f-{k}">{n}</li>' for n, k in FIELDS)
    th = "".join(f"<th>{c}</th>" for c in ["link","title","type","published_date","received_date","accepted_date","country","keywords","doi","authors","affiliations","source_page"])
    pk = ""
    for i in range(3):
        pk += f'<article class="price{" pop" if i==1 else ""}">' + (f'<span class="badge">{esc(t["pop"])}</span>' if i==1 else "") + f'<h3>{esc(t["pn"][i])}</h3><div class="amt">{PRICES[i]} <small>USD</small></div><div class="recs"><b>{RECS[i]}</b> {esc(t["recs"])}</div><p>{esc(t["inc"])}</p><button class="btn" data-pkg="{"spe"[i]}">{esc(t["pb"][i])}</button></article>'
    faq = "".join(f'<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q, a in t["fq"])
    ui = dict(dm=t["dm"], subj=t["subj"], body=t["body"], errs=t["errs"], ok=t["ok"], fail=t["fail"], none=t["none"], custom=t["custom"], opts=t["opts"], email=EMAIL)
    sd = {"@context":"https://schema.org","@graph":[
      {"@type":"Organization","name":"ResearchMeta Data","url":url(l),"email":EMAIL},
      {"@type":"WebSite","name":"ResearchMeta Data","url":url(l),"inLanguage":l},
      {"@type":"Dataset","name":"Scientific Publication Metadata Dataset","description":t["desc"],"url":url(l),"inLanguage":l,"keywords":t["kw"],"creator":{"@type":"Organization","name":"ResearchMeta Data"},"variableMeasured":[n for n,_ in FIELDS]}]}
    return f'''<!DOCTYPE html>
<html lang="{l}" data-theme="{l}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(t["title"])}</title><meta name="description" content="{esc(t["desc"])}"><meta name="keywords" content="{esc(", ".join(t["kw"]))}"><meta name="author" content="ResearchMeta Data"><meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large">
<link rel="canonical" href="{url(l)}">{alts}
<meta property="og:type" content="website"><meta property="og:site_name" content="ResearchMeta Data"><meta property="og:title" content="{esc(t["title"])}"><meta property="og:description" content="{esc(t["desc"])}"><meta property="og:url" content="{url(l)}"><meta property="og:locale" content="{l}">
<meta name="twitter:card" content="summary"><meta name="twitter:title" content="{esc(t["title"])}"><meta name="twitter:description" content="{esc(t["desc"])}">
<link rel="icon" href="{pre}assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="{pre}styles.css">
<script type="application/ld+json">{json.dumps(sd, ensure_ascii=False)}</script></head>
<body><a class="skip" href="#about">Skip to content</a>
<header class="nav"><div class="wrap bar"><a class="brand" href="#home"><svg width="30" height="30" viewBox="0 0 32 32" aria-hidden="true"><rect width="32" height="32" rx="8" fill="var(--b)"/><g fill="none" stroke="var(--c)" stroke-width="2"><path d="M8 22V10M16 22V14M24 22V8"/></g><circle cx="8" cy="10" r="2" fill="#fff"/><circle cx="16" cy="14" r="2" fill="#fff"/><circle cx="24" cy="8" r="2" fill="#fff"/></svg>ResearchMeta Data</a>
<nav id="menu" aria-label="Main">{nav}</nav>
<div class="right"><select id="lang" aria-label="Language">{langs}</select><a class="btn sm" href="#contact">{esc(t["req"])}</a><button id="burger" aria-label="Menu" aria-expanded="false">☰</button></div></div></header>
<main>
<section id="home" class="hero"><div class="wrap two"><div><h1>{esc(t["h1"])}</h1><p class="lead">{esc(t["lead"])}</p>
<div class="cta"><a class="btn" href="#sample">{esc(t["c1"])}</a><a class="btn ghost" href="#packages">{esc(t["c2"])}</a></div><div class="stats">{stats}</div></div>
<div class="viz" aria-hidden="true"><svg viewBox="0 0 420 320"><rect x="10" y="20" width="400" height="280" rx="18" fill="var(--b)"/><g fill="#ffffff22"><rect x="30" y="50" width="360" height="26" rx="6"/><rect x="30" y="86" width="360" height="26" rx="6"/><rect x="30" y="122" width="360" height="26" rx="6"/></g><g fill="var(--c)"><rect x="40" y="58" width="90" height="10" rx="3"/><rect x="40" y="94" width="130" height="10" rx="3"/><rect x="40" y="130" width="70" height="10" rx="3"/></g><g stroke="var(--a)" stroke-width="3" fill="none"><polyline points="40,270 110,225 180,245 250,190 320,205 380,165"/></g><g fill="#fff"><circle cx="110" cy="225" r="5"/><circle cx="250" cy="190" r="5"/><circle cx="380" cy="165" r="5"/></g><text x="270" y="68" fill="#fff" font-size="11" font-family="monospace">doi:10.xxxx/DEMO</text></svg></div></div></section>
<section id="sample" class="sec"><div class="wrap"><h2>{esc(t["sh"])}</h2><p class="sub">{esc(t["ss"])}</p><div class="tw" tabindex="0"><table><thead><tr>{th}</tr></thead><tbody id="rows"></tbody></table></div><p class="note">{esc(t["sd"])}</p><div class="cta"><a class="btn" href="{pre}assets/sample-data.csv" download>⬇ {esc(t["dl"])}</a><a class="btn ghost" href="#packages">{esc(t["c2"])}</a></div></div></section>
<section id="about" class="sec"><div class="wrap"><h2>{esc(t["ah"])}</h2><p class="sub">{esc(t["ap"])}</p><div class="grid4">{cards}</div>
<h2 class="mt">{esc(t["uh"])}</h2><div class="grid3">{uses}</div></div></section>
<section id="fields" class="sec alt"><div class="wrap"><h2>{esc(t["fh"])}</h2><ul class="chips">{fields}</ul><p class="note">{esc(t["fn"])}</p></div></section>
<section id="packages" class="sec alt"><div class="wrap"><h2>{esc(t["ph"])}</h2><p class="sub">{esc(t["ps"])}</p><div class="grid3 pr">{pk}</div><p class="note">{esc(t["pnote"])}</p></div></section>
<section id="faq" class="sec"><div class="wrap narrow"><h2>{esc(t["faq"])}</h2>{faq}</div></section>
<section id="contact" class="sec alt"><div class="wrap narrow"><h2>{esc(t["kh"])}</h2><p class="sub"><a class="mail" href="mailto:{EMAIL}">{EMAIL}</a> <button class="btn ghost sm" id="cpmail" type="button">{esc(t["cb"].split()[0])} ✉</button></p><p class="sub">{esc(t["kp"])}</p>
<div id="f" class="form"><label>{esc(t["lab"][0])}<input id="n" required placeholder="{esc(t["ph_"][0])}" autocomplete="name"></label><label>{esc(t["lab"][1])}<input id="e" type="email" required placeholder="{esc(t["ph_"][1])}" autocomplete="email"></label>
<label>{esc(t["lab"][2])}<input id="o" placeholder="{esc(t["ph_"][2])}"></label><label>{esc(t["lab"][3])}<select id="p"><option value="">—</option>{opts}</select></label>
<label>{esc(t["lab"][4])}<textarea id="m" rows="5" placeholder="{esc(t["ph_"][3])}"></textarea></label><p id="err" class="err" role="alert"></p><button class="btn" id="gen" type="button">{esc(t["gen"])}</button></div>
<p class="note">{esc(t["priv"])}</p>
<div id="out" class="mailcard" hidden><p><b>{esc(t["to"])}:</b> {EMAIL}</p><p><b>{esc(t["sub"])}:</b></p><pre id="os" tabindex="0"></pre><p><b>{esc(t["msg"])}:</b></p><pre id="ob" tabindex="0"></pre>
<div class="cta"><button class="btn" id="c1" type="button">{esc(t["cs"])}</button><button class="btn" id="c2" type="button">{esc(t["cb"])}</button><button class="btn ghost" id="c3" type="button">{esc(t["ca"])}</button><a class="btn" id="open" href="#">{esc(t["op"])}</a></div><p id="ok" role="status" class="ok"></p></div></div></section>
</main>
<footer class="foot"><div class="wrap"><b>ResearchMeta Data</b><p>{esc(t["fl"])}</p><nav>{"".join(f'<a href="#{i}">{esc(t["nav"][k])}</a>' for k,i in [(0,"home"),(1,"about"),(3,"sample"),(4,"packages"),(6,"contact")])}</nav>
<p><a class="mail" href="mailto:{EMAIL}">{EMAIL}</a></p><p class="small" id="licence">{esc(t["lic"])}</p><p class="small">{esc(t["disc"])}</p><p class="small">{esc(t["fd"])}</p><p class="small">{esc(t["priv"])}</p><p class="small">© <span id="yr">2026</span> ResearchMeta Data</p></div></footer>
<script type="application/json" id="i18n">{json.dumps(ui, ensure_ascii=False)}</script>
<script src="{pre}data.js" defer></script><script src="{pre}script.js" defer></script></body></html>'''

for l in LANGS:
    d = "." if l == "en" else l
    os.makedirs(d, exist_ok=True)
    open(f"{d}/index.html", "w", encoding="utf-8").write(page(l))
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
for l in LANGS:
    sm += f'<url><loc>{url(l)}</loc>' + "".join(f'<xhtml:link rel="alternate" hreflang="{x}" href="{url(x)}"/>' for x in LANGS) + f'<xhtml:link rel="alternate" hreflang="x-default" href="{url("en")}"/></url>\n'
open("sitemap.xml", "w").write(sm + "</urlset>\n")
open("robots.txt", "w").write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
print("Built for", BASE)
