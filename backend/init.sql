-- Use existing memoire database created by docker-compose
\c memoire;

-- Create categorieLivre table
CREATE TABLE IF NOT EXISTS "categorieLivre"(
    "NumCat" SERIAL PRIMARY KEY,
    "LibelleCat" VARCHAR(50) NOT NULL
);

-- Create titreEncadreur table
CREATE TABLE IF NOT EXISTS "titreEncadreur"(
    "CodeTitre" SERIAL PRIMARY KEY,
    "LibelleTitre" VARCHAR(100) NOT NULL
);

-- Create encadreurPedagogique table
CREATE TABLE IF NOT EXISTS "encadreurPedagogique"(
    "MatEncad" VARCHAR(10) PRIMARY KEY,
    "EmailEncad" VARCHAR(50),
    "MotPasseEncad" VARCHAR(70),
    "NomEncad" VARCHAR(30) NOT NULL,
    "PrenomEncad" VARCHAR(50) NOT NULL,
    "CodeTitre" INTEGER NOT NULL,
    FOREIGN KEY ("CodeTitre") REFERENCES
"titreEncadreur"("CodeTitre")
);

-- Create parcoursEtude table
CREATE TABLE IF NOT EXISTS "parcoursEtude"(
    "NumParc" SERIAL PRIMARY KEY,
    "LibelleParc" VARCHAR(50) NOT NULL
);

-- Create etudiant table
CREATE TABLE IF NOT EXISTS "etudiant"(
    "MatEtud" VARCHAR(10) PRIMARY KEY,
    "EmailEtud" VARCHAR(50),
    "MotPasseEtud" VARCHAR(70),
    "NomEtud" VARCHAR(30) NOT NULL,
    "PrenomEtud" VARCHAR(50) NOT NULL,
    "NumParc" INTEGER NOT NULL,
    FOREIGN KEY ("NumParc") REFERENCES
"parcoursEtude"("NumParc")
);

-- Create niveauEtude table
CREATE TABLE IF NOT EXISTS "niveauEtude"(
    "IdNiv" SERIAL PRIMARY KEY,
    "LibelleNiv" VARCHAR(5) NOT NULL
);

-- Create anneeUniversitaire table
CREATE TABLE IF NOT EXISTS "anneeUniversitaire"(
    "CodeAnnee" SERIAL PRIMARY KEY,
    "LibelleAnnee" VARCHAR(20) NOT NULL
);

-- Create etablissementAccueil table
CREATE TABLE IF NOT EXISTS "etablissementAccueil"(
    "IdEtab" SERIAL PRIMARY KEY,
    "Adresse" VARCHAR(100) NOT NULL,
    "Contact" VARCHAR(20) NOT NULL,
    "NomEtab" VARCHAR(100) NOT NULL,
    "Sigle" VARCHAR(30),
    "SiteWeb" VARCHAR(100)
);

-- Create livre table
CREATE TABLE IF NOT EXISTS "livre"(
    "RefLivre" SERIAL PRIMARY KEY,
    "MotCle" TEXT NOT NULL,
    "NbPage" INTEGER NOT NULL,
    "Resume" TEXT NOT NULL,
    "Theme" TEXT NOT NULL,
    "Url" VARCHAR(200) NOT NULL,
    "NumCat" INTEGER NOT NULL,
    "MatEncad" VARCHAR(10) NOT NULL,
    "IdEtab" INTEGER NOT NULL,
    "CodeAnnee" INTEGER NOT NULL,
    "IdNiv" INTEGER NOT NULL,
    FOREIGN KEY ("NumCat") REFERENCES
"categorieLivre" ("NumCat"),
    FOREIGN KEY ("MatEncad") REFERENCES
"encadreurPedagogique" ("MatEncad"),
    FOREIGN KEY ("IdEtab") REFERENCES
"etablissementAccueil" ("IdEtab"),
    FOREIGN key ("CodeAnnee") REFERENCES
"anneeUniversitaire" ("CodeAnnee"),
    FOREIGN key ("IdNiv") REFERENCES
"niveauEtude" ("IdNiv")
);

-- Create redaction (livre-etudiant) table
CREATE TABLE IF NOT EXISTS "redaction"(
    "RefLivre" INTEGER,
    "MatEtud" VARCHAR(10),
    PRIMARY KEY ("RefLivre", "MatEtud"),
    FOREIGN KEY ("RefLivre") REFERENCES
"livre"("RefLivre"),
    FOREIGN KEY ("MatEtud") REFERENCES
"etudiant"("MatEtud")
);

-- Create inscription (etudiant-niveauEtude-anneeUniversitaire) table
CREATE TABLE IF NOT EXISTS "inscription"(
    "MatEtud" VARCHAR(10),
    "IdNiv" INTEGER,
    "CodeAnnee" INTEGER,
    PRIMARY KEY ("MatEtud", "IdNiv", "CodeAnnee"),
    FOREIGN KEY ("MatEtud") REFERENCES
"etudiant" ("MatEtud"),
    FOREIGN KEY ("IdNiv") REFERENCES
"niveauEtude" ("IdNiv"),
    FOREIGN KEY ("CodeAnnee") REFERENCES
"anneeUniversitaire" ("CodeAnnee")
);

-- Some fictitious table entries
-- Entries for categorieLivre table
INSERT INTO "categorieLivre" ("LibelleCat")
VALUES
    ('Rapport de projet'),
    ('Rapport de stage'),
    ('Memoire');

-- Entries for titreEncadreur table
INSERT INTO "titreEncadreur" ("LibelleTitre")
VALUES
    ('Doctorant en informatique'),
    ('Assistant d''enseignement supérieur et de recherche'),
    ('Docteur en informatique'),
    ('Maître de conférences'),
    ('Professeur'),
    ('Professeur titulaire');

-- Entries for encadreurPedagogique table
INSERT INTO "encadreurPedagogique" ("MatEncad", "EmailEncad", "MotPasseEncad", "NomEncad", "PrenomEncad", "CodeTitre")
VALUES
    ('ENC001', 'fontainerafamant@yahoo.fr', 'fontaine', 'RAFAMANTANANTSOA', 'Fontaine', 5),
    ('ENC002', 'ralaivao.christian@gmail.com', 'christian', 'RALAIVAO', 'Christian', 2),
    ('ENC003', 'rakotoas.cyprienna@gmail.com', 'antsa', 'RAKOTOASIMBAHOAKA', 'Antsa Cyprienna', 3),
    ('ENC004', 'siakamail1@gmail.com', 'siaka', 'SIAKA', '-', 2),
    ('ENC005', NULL, NULL, 'GILANTE', 'Gesazafy', 2),
    ('ENC006', NULL, NULL, 'RANDRIANOMENJANAHARY', 'Ferdinand', 2),
    ('ENC007', NULL, NULL, 'RAZAFINDRAMONJA', 'Clément', 2),
    ('ENC008', NULL, NULL, 'RATOVONDRAHONA', 'Josué', 3),
    ('ENC009', NULL, NULL, 'RAMAMONJISOA', 'Bertin Olivier', 6),
    ('ENC010', NULL, NULL, 'RABETAFIKA', 'Louis Haja', 4),
    ('ENC011', NULL, NULL, 'RAKOTOASIMBAHOAKA', 'Cyprien Robert', 4),
    ('ENC012', NULL, NULL, 'MAHATODY', 'Thomas', 4),
    ('ENC013', NULL, NULL, 'RATIANANTITRA', 'Volatiana Marielle', 4),
    ('ENC014', NULL, NULL, 'RATIARSON', 'Venot', 4),
    ('ENC015', NULL, NULL, 'DIMBISOA', 'William Germain', 3),
    ('ENC016', NULL, NULL, 'RAZAFIMAHATRATRA', 'Hajarisena', 3),
    ('ENC017', NULL, NULL, 'KENT', 'Clark', 1);

-- Entries for parcoursEtude table
INSERT INTO "parcoursEtude" ("LibelleParc")
VALUES
    ('Génie logiciel et base de données'),
    ('Administrateur système et réseau'),
    ('Informatique général');

-- Entries for etudiant table
INSERT INTO "etudiant" ("MatEtud", "EmailEtud", "MotPasseEtud", "NomEtud", "PrenomEtud", "NumParc")
VALUES
    ('2064', 'tafitashirleyodon@gmail.com', 'shirley', 'TAFITA', 'Shirley Odon', 2),
    ('2045', NULL, NULL, 'RENEE', 'Vavy Fleurisse', 1),
    ('2047', NULL, NULL, 'KOTONIRINA', 'Ruddy Adonis', 2),
    ('2069', NULL, NULL, 'LEHIBIBY', 'Felissandro Smith', 2),
    ('2027', NULL, NULL, 'RAMIHONOSON', 'Aimé Francisco', 2),
    ('2024', NULL, NULL, 'TOMBOZAVELO', 'Jenny Phillipine', 2),
    ('2039', NULL, NULL, 'ANDRIANIRINA', 'Toky Cedric', 2),
    ('1987', NULL, NULL, 'RAMAHALIARIVO', 'Lanja Iarinaly', 2),
    ('831-HF', NULL, NULL, 'SAMBANY', 'Michel Laurenzio', 3),
    ('795-HF', NULL, NULL, 'NOELSON', 'Donnatien Jean Hervé', 3),
    ('846-HF', NULL, NULL, 'RABETO', 'Mac Manfred Hardy', 3),
    ('2056', NULL, NULL, 'VALITERA', 'Fehizoroniaina Indrafonjanahary', 1),
    ('2044', NULL, NULL, 'FETIARISON', 'Jules Michel', 1);


-- Entries for niveauEtude table
INSERT INTO "niveauEtude" ("LibelleNiv")
VALUES
    ('L1'),
    ('L2'),
    ('L3'),
    ('M1'),
    ('M2');

-- Entries for anneeUniversitaire table
INSERT INTO "anneeUniversitaire" ("LibelleAnnee")
VALUES
    ('2018-2019'),
    ('2019-2020'),
    ('2020-2021'),
    ('2021-2022'),
    ('2022-2023'),
    ('2023-2024');

-- Entries for etablissementAccueil table
INSERT INTO "etablissementAccueil" ("Adresse", "Contact", "NomEtab", "Sigle", "SiteWeb")
VALUES
    ('Tanambao Fianarantsoa', '+261340573336', 'Ecole Nationale d''Informatique', 'ENI', NULL),
    ('5, Rue Ampasamazava Est, Toamasina', '+261347179024', 'Société de Manutention de Marchandises Conventionnelles', 'SMMC', NULL),
    ('Rue du commerce No.10, Toamasina', '+261205335204', 'Madagascar International Container Terminal Services Ltd.', 'MICTSL', 'www.mictsl.mg'),
    ('Lot II J 17 TER, Antananarivo', '+261321125700', 'Agence Portuaire Maritime et Fluvial', 'APMF', 'www.apmf.mg'),
    ('Lot III L 49 G,Tsimbazaza, Antananarivo', '+261341130455', 'Numen Madagascar', NULL, 'www.numenmadagascar.com'),
    ('Les Rosiers Antsahavola, 1ere étage, Antananarivo', '+261347188545', 'Hellotana', NULL, 'www.hellotana.com'),
    ('15 Bis, Boulevard De La Fidelite, Toamasina', '+261340230940', 'L''Assistance et Maintenance Informatique', 'L''AMInformatique', NULL),
    ('Bloc Administratif Tsianolondroa, Fianarantsoa', '+261321201061', 'Direction Régionale de Fianarantsoa', NULL, NULL),
    ('Enceinte portuaire de Toamasina', '+261205332155', 'Société du Port à gestion Autonome de Tamatave', 'SPAT', NULL),
    ('La Tour, Rue Ravoninahitriniarivo, Ankorondrano, Antananarivo', '+261320718468', 'Orange Digital Center', 'ODC', 'www.orangedigitalcenters.com'),
    ('Lot IVP Près 40 Zone Zapa Tana Water Front, Ambodivona', '+261321165900', 'MANAO', NULL, 'www.manao.eu'),
    ('Campus Telma, Zone Galaxy Andraharo, Antananarivo', '+261340000800', 'Telecom Malagasy', 'TELMA', 'www.telma.mg'),
    ('Immeuble Aquamad, Route du Pape, Morarano - Alarobia Antananarivo', '+261202253604', 'ETECH', NULL, 'www.etechconsulting-mg.com'),
    ('Lot Villa Papringo, Isaha Fianarantsoa', '+261346757384', 'AKATA Goavana', NULL, 'www.akata-goavana.com'),
    ('Antananarivo', '+261347755834', 'RELIA Consulting', NULL, 'www.relia-consulting.com'),
    ('Lot 138AB/fr 3502 Ambany lalana, Fianarantsoa', '+261349881619', 'ARATO', NULL, 'www.arato.mg'),
    ('9, Rue Johns et Bevan Anjoma, Toamasina', '+261323366565', 'Dynatec Madagascar Societe Anonyme', 'DMSA', 'www.ambatovy.mg');

-- Entries for livre table
INSERT INTO "livre" ("MotCle", "NbPage", "Resume", "Theme", "Url", "NumCat", "MatEncad", "IdEtab", "CodeAnnee", "IdNiv")
VALUES
    ('Arduino, automatisation, carrefour, feu tricolore, prototypage, simulation', 50, 'Occaecat do duis magna mollit amet voluptate dolore veniam pariatur. Exercitation sint veniam mollit ullamco mollit eiusmod mollit cupidatat eu enim cupidatat. Velit ipsum ex consequat reprehenderit duis. Velit irure nulla minim sunt. Et aliqua est et aliqua nisi consequat irure deserunt. Laborum minim esse pariatur cupidatat proident ex aute anim do aliqua dolor occaecat fugiat deserunt. Consectetur est proident aliquip id labore consectetur ea tempor aliqua velit id ullamco.', 'Création d''un prototype de simulation de feu tricolores sur un carrefour avec Arduino', 'www.livre1.com', 1, 'ENC004', 1, 1, 1),

    ('Arduino, automatisation, BMP180, capteur de pression, dépression atmosphérique, I2C', 40, 'Occaecat do duis magna mollit amet voluptate dolore veniam pariatur. Exercitation sint veniam mollit ullamco mollit eiusmod mollit cupidatat eu enim cupidatat. Velit ipsum ex consequat reprehenderit duis. Velit irure nulla minim sunt. Et aliqua est et aliqua nisi consequat irure deserunt. Laborum minim esse pariatur cupidatat proident ex aute anim do aliqua dolor occaecat fugiat deserunt. Consectetur est proident aliquip id labore consectetur ea tempor aliqua velit id ullamco.', 'Détection de dépression atmosphérique en utilisant Arduino', 'www.livre2.com', 1, 'ENC005', 1, 1, 1),

    ('Automatisation, capteurs, contrôle à distance, domotique, économie d''énergie, protocoles', 45, 'Occaecat do duis magna mollit amet voluptate dolore veniam pariatur. Exercitation sint veniam mollit ullamco mollit eiusmod mollit cupidatat eu enim cupidatat. Velit ipsum ex consequat reprehenderit duis. Velit irure nulla minim sunt. Et aliqua est et aliqua nisi consequat irure deserunt. Laborum minim esse pariatur cupidatat proident ex aute anim do aliqua dolor occaecat fugiat deserunt. Consectetur est proident aliquip id labore consectetur ea tempor aliqua velit id ullamco.', 'Maison intelligente basé sur Arduino', 'www.livre3.com', 1, 'ENC007', 1, 1, 1),

    ('Billet, gestion, numérique, QT, train', 52, 'Occaecat do duis magna mollit amet voluptate dolore veniam pariatur. Exercitation sint veniam mollit ullamco mollit eiusmod mollit cupidatat eu enim cupidatat. Velit ipsum ex consequat reprehenderit duis. Velit irure nulla minim sunt. Et aliqua est et aliqua nisi consequat irure deserunt. Laborum minim esse pariatur cupidatat proident ex aute anim do aliqua dolor occaecat fugiat deserunt. Consectetur est proident aliquip id labore consectetur ea tempor aliqua velit id ullamco.', 'Gestion de billet de train en QT', 'www.livre4.com', 1, 'ENC008', 1, 1, 1),

    ('Administration, gestion, personnel, ressources humaines, SIRH', 35, 'Occaecat do duis magna mollit amet voluptate dolore veniam pariatur. Exercitation sint veniam mollit ullamco mollit eiusmod mollit cupidatat eu enim cupidatat. Velit ipsum ex consequat reprehenderit duis. Velit irure nulla minim sunt. Et aliqua est et aliqua nisi consequat irure deserunt. Laborum minim esse pariatur cupidatat proident ex aute anim do aliqua dolor occaecat fugiat deserunt. Consectetur est proident aliquip id labore consectetur ea tempor aliqua velit id ullamco.', 'Gestion de personnel en QT', 'www.livre5.com', 1, 'ENC013', 1, 1, 1),

    ('Application, base de données, étudiants, gestion, interface graphique, Qt, système', 48, 'Occaecat do duis magna mollit amet voluptate dolore veniam pariatur. Exercitation sint veniam mollit ullamco mollit eiusmod mollit cupidatat eu enim cupidatat. Velit ipsum ex consequat reprehenderit duis. Velit irure nulla minim sunt. Et aliqua est et aliqua nisi consequat irure deserunt. Laborum minim esse pariatur cupidatat proident ex aute anim do aliqua dolor occaecat fugiat deserunt. Consectetur est proident aliquip id labore consectetur ea tempor aliqua velit id ullamco.', 'Gestion de note en QT', 'www.livre6.com', 1, 'ENC011', 1, 1, 1),

    ('Automatisation, configurations, IP, mapping, performances, réseau, surveillance, switch', 57, 'Occaecat do duis magna mollit amet voluptate dolore veniam pariatur. Exercitation sint veniam mollit ullamco mollit eiusmod mollit cupidatat eu enim cupidatat. Velit ipsum ex consequat reprehenderit duis. Velit irure nulla minim sunt. Et aliqua est et aliqua nisi consequat irure deserunt. Laborum minim esse pariatur cupidatat proident ex aute anim do aliqua dolor occaecat fugiat deserunt. Consectetur est proident aliquip id labore consectetur ea tempor aliqua velit id ullamco.', 'Supervision réseau et système avec Solarwind', 'www.livre7.com', 2, 'ENC004', 3, 2, 2),

    ('Configurations, hôtes, IP, ports, réseau, trafic, virtuels', 40, 'Occaecat do duis magna mollit amet voluptate dolore veniam pariatur. Exercitation sint veniam mollit ullamco mollit eiusmod mollit cupidatat eu enim cupidatat. Velit ipsum ex consequat reprehenderit duis. Velit irure nulla minim sunt. Et aliqua est et aliqua nisi consequat irure deserunt. Laborum minim esse pariatur cupidatat proident ex aute anim do aliqua dolor occaecat fugiat deserunt. Consectetur est proident aliquip id labore consectetur ea tempor aliqua velit id ullamco.', 'Mise en place d''un serveur de messagerie sous Ubuntu', 'www.livre8.com', 2, 'ENC001', 11, 2, 2),

    ('Analyse, IDS, IPS, installation, prévention, réseau, Snort, trafic', 36, 'Occaecat do duis magna mollit amet voluptate dolore veniam pariatur. Exercitation sint veniam mollit ullamco mollit eiusmod mollit cupidatat eu enim cupidatat. Velit ipsum ex consequat reprehenderit duis. Velit irure nulla minim sunt. Et aliqua est et aliqua nisi consequat irure deserunt. Laborum minim esse pariatur cupidatat proident ex aute anim do aliqua dolor occaecat fugiat deserunt. Consectetur est proident aliquip id labore consectetur ea tempor aliqua velit id ullamco.', 'Détection d''intrusion avec Snort', 'www.livre9.com', 2, 'ENC006', 14, 2, 2),

    ('Agence, application, développement, merise, MySQL, PHP', 61, 'Occaecat do duis magna mollit amet voluptate dolore veniam pariatur. Exercitation sint veniam mollit ullamco mollit eiusmod mollit cupidatat eu enim cupidatat. Velit ipsum ex consequat reprehenderit duis. Velit irure nulla minim sunt. Et aliqua est et aliqua nisi consequat irure deserunt. Laborum minim esse pariatur cupidatat proident ex aute anim do aliqua dolor occaecat fugiat deserunt. Consectetur est proident aliquip id labore consectetur ea tempor aliqua velit id ullamco.', 'Conception et réalisation d''une application Web de gestion de voyages en PHP et MySQL', 'www.livre10.com', 2, 'ENC014', 16, 2, 2),

    ('Caisses, C++, Conception, postgreSQL, projet, web', 66, 'Occaecat do duis magna mollit amet voluptate dolore veniam pariatur. Exercitation sint veniam mollit ullamco mollit eiusmod mollit cupidatat eu enim cupidatat. Velit ipsum ex consequat reprehenderit duis. Velit irure nulla minim sunt. Et aliqua est et aliqua nisi consequat irure deserunt. Laborum minim esse pariatur cupidatat proident ex aute anim do aliqua dolor occaecat fugiat deserunt. Consectetur est proident aliquip id labore consectetur ea tempor aliqua velit id ullamco.', 'Conception d''une application web de gestion de caisses en C++ et PostgreSQL', 'www.livre11.com', 2, 'ENC009', 2, 2, 2),

    ('Apache2, debian, installation, PHP, serveur, web', 43, 'Occaecat do duis magna mollit amet voluptate dolore veniam pariatur. Exercitation sint veniam mollit ullamco mollit eiusmod mollit cupidatat eu enim cupidatat. Velit ipsum ex consequat reprehenderit duis. Velit irure nulla minim sunt. Et aliqua est et aliqua nisi consequat irure deserunt. Laborum minim esse pariatur cupidatat proident ex aute anim do aliqua dolor occaecat fugiat deserunt. Consectetur est proident aliquip id labore consectetur ea tempor aliqua velit id ullamco.', 'Mise en place d''un serveur web sous Debian', 'www.livre12.com', 2, 'ENC002', 5, 2, 2),

    ('Carte réseau, CPL, ethernet, FAI, HTTP, intranet, LAN', 70, 'Occaecat do duis magna mollit amet voluptate dolore veniam pariatur. Exercitation sint veniam mollit ullamco mollit eiusmod mollit cupidatat eu enim cupidatat. Velit ipsum ex consequat reprehenderit duis. Velit irure nulla minim sunt. Et aliqua est et aliqua nisi consequat irure deserunt. Laborum minim esse pariatur cupidatat proident ex aute anim do aliqua dolor occaecat fugiat deserunt. Consectetur est proident aliquip id labore consectetur ea tempor aliqua velit id ullamco.', 'Restructuration, optimisation et sécurisation du réseau local au niveau du siège social', 'www.livre13.com', 3, 'ENC003', 2, 3, 3),

    ('Centralisation, litiges, marketplace, transaction, UML', 73, 'Occaecat do duis magna mollit amet voluptate dolore veniam pariatur. Exercitation sint veniam mollit ullamco mollit eiusmod mollit cupidatat eu enim cupidatat. Velit ipsum ex consequat reprehenderit duis. Velit irure nulla minim sunt. Et aliqua est et aliqua nisi consequat irure deserunt. Laborum minim esse pariatur cupidatat proident ex aute anim do aliqua dolor occaecat fugiat deserunt. Consectetur est proident aliquip id labore consectetur ea tempor aliqua velit id ullamco.', 'Conception et réalisation d''outils web pour la gestion des litiges et la centralisation des e-mails transactionnels pour la marketplace', 'www.livre14.com', 3, 'ENC012', 6, 3, 3),

    ('Catalogue, e-commerce, marketplace, plateforme, transactions, vente en ligne', 57, 'Occaecat do duis magna mollit amet voluptate dolore veniam pariatur. Exercitation sint veniam mollit ullamco mollit eiusmod mollit cupidatat eu enim cupidatat. Velit ipsum ex consequat reprehenderit duis. Velit irure nulla minim sunt. Et aliqua est et aliqua nisi consequat irure deserunt. Laborum minim esse pariatur cupidatat proident ex aute anim do aliqua dolor occaecat fugiat deserunt. Consectetur est proident aliquip id labore consectetur ea tempor aliqua velit id ullamco.', 'Conception et réalisation d''une plateforme pour la marketplace', 'www.livre15.com', 3, 'ENC012', 13, 3, 3),

    ('Automatisation, cartographie, flux de travail, intelligence artificielle, optimisation, RPA, workflow', 63, 'Occaecat do duis magna mollit amet voluptate dolore veniam pariatur. Exercitation sint veniam mollit ullamco mollit eiusmod mollit cupidatat eu enim cupidatat. Velit ipsum ex consequat reprehenderit duis. Velit irure nulla minim sunt. Et aliqua est et aliqua nisi consequat irure deserunt. Laborum minim esse pariatur cupidatat proident ex aute anim do aliqua dolor occaecat fugiat deserunt. Consectetur est proident aliquip id labore consectetur ea tempor aliqua velit id ullamco.', 'Conception et réalisation d''un système de gestion de l''automatisation des tâche', 'www.livre16.com', 3, 'ENC012', 15, 3, 3),

    ('Automatisation, CI/CD, conteneurs, infrastructure as Code, orchestration, scalabilité', 59, 'Occaecat do duis magna mollit amet voluptate dolore veniam pariatur. Exercitation sint veniam mollit ullamco mollit eiusmod mollit cupidatat eu enim cupidatat. Velit ipsum ex consequat reprehenderit duis. Velit irure nulla minim sunt. Et aliqua est et aliqua nisi consequat irure deserunt. Laborum minim esse pariatur cupidatat proident ex aute anim do aliqua dolor occaecat fugiat deserunt. Consectetur est proident aliquip id labore consectetur ea tempor aliqua velit id ullamco.', 'Integration et deployment continue vers Kubernetes', 'www.livre17.com', 3, 'ENC001', 16, 3, 3),

    ('Automatisation, evaluation, interface utilisateur, ressources humaines, technologie moderne', 85, 'Occaecat do duis magna mollit amet voluptate dolore veniam pariatur. Exercitation sint veniam mollit ullamco mollit eiusmod mollit cupidatat eu enim cupidatat. Velit ipsum ex consequat reprehenderit duis. Velit irure nulla minim sunt. Et aliqua est et aliqua nisi consequat irure deserunt. Laborum minim esse pariatur cupidatat proident ex aute anim do aliqua dolor occaecat fugiat deserunt. Consectetur est proident aliquip id labore consectetur ea tempor aliqua velit id ullamco.', 'Conception et réalisation d''une application web pour l''évaluation du personnel', 'www.livre18.com', 3, 'ENC002', 4, 3, 3),

    ('Cisco, configuration, GNS3, IOS, netmiko, OSPF, python3, routeurs, topologie', 60, 'Occaecat do duis magna mollit amet voluptate dolore veniam pariatur. Exercitation sint veniam mollit ullamco mollit eiusmod mollit cupidatat eu enim cupidatat. Velit ipsum ex consequat reprehenderit duis. Velit irure nulla minim sunt. Et aliqua est et aliqua nisi consequat irure deserunt. Laborum minim esse pariatur cupidatat proident ex aute anim do aliqua dolor occaecat fugiat deserunt. Consectetur est proident aliquip id labore consectetur ea tempor aliqua velit id ullamco.', 'Automatisation réseau avec Netmiko', 'www.livre19.com', 1, 'ENC004', 1, 4, 4),

    ('Disponibilité, pannes, protocoles, réseau, routeurs, STP, virtual Gateway', 51, 'Occaecat do duis magna mollit amet voluptate dolore veniam pariatur. Exercitation sint veniam mollit ullamco mollit eiusmod mollit cupidatat eu enim cupidatat. Velit ipsum ex consequat reprehenderit duis. Velit irure nulla minim sunt. Et aliqua est et aliqua nisi consequat irure deserunt. Laborum minim esse pariatur cupidatat proident ex aute anim do aliqua dolor occaecat fugiat deserunt. Consectetur est proident aliquip id labore consectetur ea tempor aliqua velit id ullamco.', 'Mise en place d''un réseau hautement disponible', 'www.livre20.com', 1, 'ENC007', 1, 4, 4),

    ('Agile, backlog, brainstorming, jalons, PERT, planification', 62, 'Occaecat do duis magna mollit amet voluptate dolore veniam pariatur. Exercitation sint veniam mollit ullamco mollit eiusmod mollit cupidatat eu enim cupidatat. Velit ipsum ex consequat reprehenderit duis. Velit irure nulla minim sunt. Et aliqua est et aliqua nisi consequat irure deserunt. Laborum minim esse pariatur cupidatat proident ex aute anim do aliqua dolor occaecat fugiat deserunt. Consectetur est proident aliquip id labore consectetur ea tempor aliqua velit id ullamco.', 'Conception et réalisation d''une application mobile de planification de taches', 'www.livre21.com', 1, 'ENC016', 1, 4, 4),

    ('Algorithmes, apprentissage automatique, intelligence artificielle, python, réseaux de neurones, traitement d''image', 53, 'Occaecat do duis magna mollit amet voluptate dolore veniam pariatur. Exercitation sint veniam mollit ullamco mollit eiusmod mollit cupidatat eu enim cupidatat. Velit ipsum ex consequat reprehenderit duis. Velit irure nulla minim sunt. Et aliqua est et aliqua nisi consequat irure deserunt. Laborum minim esse pariatur cupidatat proident ex aute anim do aliqua dolor occaecat fugiat deserunt. Consectetur est proident aliquip id labore consectetur ea tempor aliqua velit id ullamco.', 'Conception et réalisation d''une application web de détection de visage en Python', 'www.livre22.com', 1, 'ENC006', 1, 4, 4),

    ('Algorithmes, analyse de données, application mobile, intelligence artificielle, modélisation, prédiction, visualisation', 47, 'Occaecat do duis magna mollit amet voluptate dolore veniam pariatur. Exercitation sint veniam mollit ullamco mollit eiusmod mollit cupidatat eu enim cupidatat. Velit ipsum ex consequat reprehenderit duis. Velit irure nulla minim sunt. Et aliqua est et aliqua nisi consequat irure deserunt. Laborum minim esse pariatur cupidatat proident ex aute anim do aliqua dolor occaecat fugiat deserunt. Consectetur est proident aliquip id labore consectetur ea tempor aliqua velit id ullamco.', 'Conception et réalisation d''une application intelligente de prédiction de coût d''un terrain', 'www.livre23.com', 1, 'ENC008', 1, 4, 4),

    ('Android, attaque, malware, pré-installation, sécurité, smartphones, système', 55, 'Occaecat do duis magna mollit amet voluptate dolore veniam pariatur. Exercitation sint veniam mollit ullamco mollit eiusmod mollit cupidatat eu enim cupidatat. Velit ipsum ex consequat reprehenderit duis. Velit irure nulla minim sunt. Et aliqua est et aliqua nisi consequat irure deserunt. Laborum minim esse pariatur cupidatat proident ex aute anim do aliqua dolor occaecat fugiat deserunt. Consectetur est proident aliquip id labore consectetur ea tempor aliqua velit id ullamco.', 'Attaque et prise de control d''un system Android', 'www.livre24.com', 1, 'ENC001', 1, 4, 4),

    ('Attaque de brèche, attaque DoS, cybercriminalité, espionnage, infection Monkey, rançongiciels, vulnérabilités', 95, 'Occaecat do duis magna mollit amet voluptate dolore veniam pariatur. Exercitation sint veniam mollit ullamco mollit eiusmod mollit cupidatat eu enim cupidatat. Velit ipsum ex consequat reprehenderit duis. Velit irure nulla minim sunt. Et aliqua est et aliqua nisi consequat irure deserunt. Laborum minim esse pariatur cupidatat proident ex aute anim do aliqua dolor occaecat fugiat deserunt. Consectetur est proident aliquip id labore consectetur ea tempor aliqua velit id ullamco.', 'Outils et techniques d''attaque en cybersécurité', 'www.livre25.com', 3, 'ENC001', 1, 5, 5),

    ('Agilité, automatisation, micro-services, optimisation des processus, synchronisation', 87, 'Occaecat do duis magna mollit amet voluptate dolore veniam pariatur. Exercitation sint veniam mollit ullamco mollit eiusmod mollit cupidatat eu enim cupidatat. Velit ipsum ex consequat reprehenderit duis. Velit irure nulla minim sunt. Et aliqua est et aliqua nisi consequat irure deserunt. Laborum minim esse pariatur cupidatat proident ex aute anim do aliqua dolor occaecat fugiat deserunt. Consectetur est proident aliquip id labore consectetur ea tempor aliqua velit id ullamco.', 'Etude et mise en place d''une infrastructure Devops', 'www.livre26.com', 3, 'ENC005', 9, 5, 5),

    ('Client, Hellopromail, optimisation, satisfaction', 102, 'Occaecat do duis magna mollit amet voluptate dolore veniam pariatur. Exercitation sint veniam mollit ullamco mollit eiusmod mollit cupidatat eu enim cupidatat. Velit ipsum ex consequat reprehenderit duis. Velit irure nulla minim sunt. Et aliqua est et aliqua nisi consequat irure deserunt. Laborum minim esse pariatur cupidatat proident ex aute anim do aliqua dolor occaecat fugiat deserunt. Consectetur est proident aliquip id labore consectetur ea tempor aliqua velit id ullamco.', 'Mise en place du service Hellopromail pour l''optimisation de la satisfaction client', 'www.livre27.com', 3, 'ENC013', 6, 5, 5),

    ('E-réputation, gestion, médias sociaux, plateforme, stratégie d''e-réputation, User Generated Content', 111, 'Occaecat do duis magna mollit amet voluptate dolore veniam pariatur. Exercitation sint veniam mollit ullamco mollit eiusmod mollit cupidatat eu enim cupidatat. Velit ipsum ex consequat reprehenderit duis. Velit irure nulla minim sunt. Et aliqua est et aliqua nisi consequat irure deserunt. Laborum minim esse pariatur cupidatat proident ex aute anim do aliqua dolor occaecat fugiat deserunt. Consectetur est proident aliquip id labore consectetur ea tempor aliqua velit id ullamco.', 'Mise en place d''une plateforme de e-réputation', 'www.livre28.com', 3, 'ENC003', 12, 5, 5),

    ('Capteurs, données, énergie, intelligence artificielle, réseaux, smart infrastructure', 98, 'Occaecat do duis magna mollit amet voluptate dolore veniam pariatur. Exercitation sint veniam mollit ullamco mollit eiusmod mollit cupidatat eu enim cupidatat. Velit ipsum ex consequat reprehenderit duis. Velit irure nulla minim sunt. Et aliqua est et aliqua nisi consequat irure deserunt. Laborum minim esse pariatur cupidatat proident ex aute anim do aliqua dolor occaecat fugiat deserunt. Consectetur est proident aliquip id labore consectetur ea tempor aliqua velit id ullamco.', 'Création d''une infrastructure intelligente : développement efficace', 'www.livre29.com', 3, 'ENC005', 10, 5, 5),

    ('Carrière, étudiants, France, Méthode agile, plateforme, projet, réalisation', 109, 'Occaecat do duis magna mollit amet voluptate dolore veniam pariatur. Exercitation sint veniam mollit ullamco mollit eiusmod mollit cupidatat eu enim cupidatat. Velit ipsum ex consequat reprehenderit duis. Velit irure nulla minim sunt. Et aliqua est et aliqua nisi consequat irure deserunt. Laborum minim esse pariatur cupidatat proident ex aute anim do aliqua dolor occaecat fugiat deserunt. Consectetur est proident aliquip id labore consectetur ea tempor aliqua velit id ullamco.', 'Conception et réalisation d''une plateforme de carrière pour les étudiants en France', 'www.livre30.com', 3, 'ENC016', 15, 5, 5);

-- Entries for redaction (livre-etudiant) table
INSERT INTO "redaction" ("RefLivre", "MatEtud")
VALUES
    (1, '2064'), (1, '2027'), (1, '2024'),
    (2, '2069'), (2, '2047'),
    (3, '2039'), (3, '1987'),
    (4, '831-HF'), (4, '795-HF'),
    (5, '2045'), (5, '2044'),
    (6, '2056'),
    (7, '2064'), (7, '2047'),
    (8, '2027'), (8, '2024'),
    (9, '2039'), (9, '1987'),
    (10, '2045'), (10, '2044'),
    (11, '831-HF'), (11, '795-HF'),
    (12, '846-HF'),
    (13, '2064'),
    (14, '831-HF'),
    (15, '2044'),
    (16, '846-HF'),
    (17, '1987'),
    (18, '2045'),
    (19, '2064'), (19, '2047'),
    (20, '2027'), (20, '2024'),
    (21, '831-HF'), (21, '795-HF'),
    (22, '2039'), (22, '1987'),
    (23, '2045'), (23, '2044'),
    (24, '2069'),
    (25, '2069'),
    (26, '2024'),
    (27, '2056'),
    (28, '831-HF'),
    (29, '846-HF'),
    (30, '2045');

-- Entries for inscription (etudiant-niveauEtude-anneeUniversitaire) table
INSERT INTO "inscription" ("MatEtud", "IdNiv", "CodeAnnee")
VALUES
    ('2064', 1, 1), ('2045', 1, 1), ('2047', 1, 1), ('2069', 1, 1), ('2027', 1, 1), ('2024', 1, 1), ('2039', 1, 1), ('1987', 1, 1), ('831-HF', 1, 1), ('795-HF', 1, 1), ('846-HF', 1, 1), ('2056', 1, 1), ('2044', 1, 1),

    ('2064', 2, 2), ('2045', 2, 2), ('2047', 2, 2), ('2069', 2, 2), ('2027', 2, 2), ('2024', 2, 2), ('2039', 2, 2), ('1987', 2, 2), ('831-HF', 2, 2), ('795-HF', 2, 2), ('846-HF', 2, 2), ('2056', 2, 2), ('2044', 2, 2),

    ('2064', 3, 3), ('2045', 3, 3), ('2047', 3, 3), ('2069', 3, 3), ('2027', 3, 3), ('2024', 3, 3), ('2039', 3, 3), ('1987', 3, 3), ('831-HF', 3, 3), ('795-HF', 3, 3), ('846-HF', 3, 3), ('2056', 3, 3), ('2044', 3, 3),

    ('2064', 4, 4), ('2045', 4, 4), ('2047', 4, 4), ('2069', 4, 4), ('2027', 4, 4), ('2024', 4, 4), ('2039', 4, 4), ('1987', 4, 4), ('831-HF', 4, 4), ('795-HF', 4, 4), ('846-HF', 4, 4), ('2056', 4, 4), ('2044', 4, 4),

    ('2064', 5, 5), ('2045', 5, 5), ('2047', 5, 5), ('2069', 5, 5), ('2027', 5, 5), ('2024', 5, 5), ('2039', 5, 5), ('1987', 5, 5), ('831-HF', 5, 5), ('795-HF', 5, 5), ('846-HF', 5, 5), ('2056', 5, 5), ('2044', 5, 5);
