﻿-- PURGE DES DONNEES : DEBUT;
-- Purge des tables de données brutes;
DELETE FROM [PREFIXE]bati;
DELETE FROM [PREFIXE]fanr;
DELETE FROM [PREFIXE]lloc;
DELETE FROM [PREFIXE]nbat;
DELETE FROM [PREFIXE]pdll;
DELETE FROM [PREFIXE]prop;
-- Purge des tables de données;
DELETE FROM [PREFIXE]voie where annee='[ANNEE]';
DELETE FROM [PREFIXE]commune where annee='[ANNEE]';
DELETE FROM [PREFIXE]lotslocaux where annee='[ANNEE]';
DELETE FROM [PREFIXE]lots where annee='[ANNEE]';
DELETE FROM [PREFIXE]parcellecomposante where annee='[ANNEE]';
DELETE FROM [PREFIXE]pdl where annee='[ANNEE]';
DELETE FROM [PREFIXE]comptecommunal where annee='[ANNEE]';
DELETE FROM [PREFIXE]proprietaire where annee='[ANNEE]';
DELETE FROM [PREFIXE]pevdependances where annee='[ANNEE]';
DELETE FROM [PREFIXE]pevprofessionnelle where annee='[ANNEE]';
DELETE FROM [PREFIXE]pevprincipale where annee='[ANNEE]';
DELETE FROM [PREFIXE]pevtaxation where annee='[ANNEE]';
DELETE FROM [PREFIXE]pevexoneration where annee='[ANNEE]';
DELETE FROM [PREFIXE]pev where annee='[ANNEE]';
DELETE FROM [PREFIXE]local10 where annee='[ANNEE]';
DELETE FROM [PREFIXE]local00 where annee='[ANNEE]';
DELETE FROM [PREFIXE]suftaxation where annee='[ANNEE]';
DELETE FROM [PREFIXE]sufexoneration where annee='[ANNEE]';
DELETE FROM [PREFIXE]suf where annee='[ANNEE]';
DELETE FROM [PREFIXE]parcelle where annee='[ANNEE]';
-- PURGE DES DONNEES : FIN;