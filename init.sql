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
    "MotPasseEncad" VARCHAR(50),
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
    "MotPasseEtud" VARCHAR(50),
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
    "MotCle" VARCHAR(100) NOT NULL,
    "NbPage" INTEGER NOT NULL,
    "Resume" TEXT NOT NULL,
    "Theme" VARCHAR(100) NOT NULL,
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
    ('Doctorant'),
    ('Assistant de recherche'),
    ('Docteur'),
    ('Maître de conférences'),
    ('Professeur'),
    ('Professeur titulaire');

-- Entries for encadreurPedagogique table
INSERT INTO "encadreurPedagogique" ("MatEncad", "EmailEncad", "MotPasseEncad", "NomEncad", "PrenomEncad", "CodeTitre")
VALUES
    ('ENC001', 'encadreur1@email.com', 'motdepasse1', 'Smith', 'John', 1),
    ('ENC002', 'encadreur2@email.com', 'motdepasse2', 'Johnson', 'Emily', 2),
    ('ENC003', 'encadreur3@email.com', 'motdepasse3', 'Williams', 'Michael', 3);

-- Entries for parcoursEtude table
INSERT INTO "parcoursEtude" ("LibelleParc")
VALUES
    ('Génie logiciel et base de données'),
    ('Administrateur système et réseau'),
    ('Informatique général');

-- Entries for etudiant table
INSERT INTO "etudiant" ("MatEtud", "EmailEtud", "MotPasseEtud", "NomEtud", "PrenomEtud", "NumParc")
VALUES
    ('ETU001', 'etudiant1@email.com', 'motdepasse1', 'Martin', 'Sarah', 1),
    ('ETU002', 'etudiant2@email.com', 'motdepasse2', 'Anderson', 'David', 2),
    ('ETU003', NULL, NULL, 'Rodriguez', 'Maria', 3);

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
    ('123 Rue de l''Université', '0320200202', 'EntrepriseA', 'EA', 'www.entreprisea.com'),
    ('456 Avenue des Sciences', '0320300303', 'EntrepriseB', 'EB', 'www.entrepriseb.com'),
    ('789 Boulevard des Arts', '0320400404', 'EntrepriseC', 'EC', 'www.entreprisec.com');

-- Entries for livre table
INSERT INTO "livre" ("MotCle", "NbPage", "Resume", "Theme", "Url", "NumCat", "MatEncad", "IdEtab", "CodeAnnee", "IdNiv")
VALUES
    ('Quelques mots clés', 80, 'Un super resumé', 'Administration d''un réseau local', 'www.livre1.com', 1, 'ENC001', 1, 1, 1),
    ('Liste de mots clés', 100, 'Un bel resumé', 'Application de gestion de stock', 'www.livre2.com', 2, 'ENC002', 2, 2, 2),
    ('Mots clés', 120, 'Quel resumé', 'Intelligence artificielle', 'www.livre3.com', 1, 'ENC003', 3, 3, 3);

-- Entries for redaction (livre-etudiant) table
INSERT INTO "redaction" ("RefLivre", "MatEtud")
VALUES
    (1, 'ETU001'),
    (2, 'ETU002'),
    (3, 'ETU003');

-- Entries for inscription (etudiant-niveauEtude-anneeUniversitaire) table
INSERT INTO "inscription" ("MatEtud", "IdNiv", "CodeAnnee")
VALUES
    ('ETU001', 1, 1),
    ('ETU002', 2, 2),
    ('ETU003', 3, 3);
