# -*- coding: utf-8 -*-
from create_db import Info, Drawing

from sqlalchemy import *
from sqlalchemy.orm import relation, sessionmaker

engine = create_engine('sqlite:///db.sql')

Session = sessionmaker(bind=engine)
session = Session()

# FIXME: permettre de rentrer des données avec des accents

i1 = Info("Mediatheque", "Ouverte depuis le 28 aout 2012, elle fonctionne sous la responsabilite de Veronique Lelion. Le nom a ete choisi par le conseil municipal apres sondage aupres de la population. Il associe la fonction premiere du batiment avec sa fonction actuelle. Un fonds documentaire de plus de 5000 ouvrages est a la disposition du public.")
i2 = Info("Gymnase", "Activites tennis, badminton, handball, basket-ball, ... Acces autorise avec  badge apres inscription en mairie. Reglement du gymnase: Reglement")
i3 = Info("Village de la radio", "Autrefois la baie de Houistreham etait un large estuaire ou la mer 'Ocean britannique' s'avancait de 16 kilometres a l'interieur des terres. Apres la conquete de la Gaule par Cesar, en 51 avant J.C., les Romains s'installerent dans la region et edifierent des fortifications pour assurer leur defense et proteger les voies de communication. A cette epoque la capitale des viducasses etait Araguenaue (aujourd'hui la commune de Vieux), ville riche au sud-ouest de Caen. Caen, en bordure de l'Odon, n'etait qu'un petit village. De nombreuses voies romaines parcouraient la region. L'une d'entre elles allait de Bayeux a Benouville en passant par Reviers et Douvres. Une autre, souvent empruntee par des pelerins, se rendait a la Delyvrande, lieu de pelerinage important, passant au sud de Bernieres en un lieu nomme Saint Ursin. Epron se trouvait dans un triangle forme par la voie Bayeux - Benouville et la voie Saint Come a Vieux. Un tres ancien chemin, trace en ligne droite partait d'une source dite miraculeuse a Saint Clair, longeait une villa gallo-romaine, traversait Lebisey puis Epron, passait par le lieu dit 'La Croix Cantee' (Epron) et se prolongeait vers Cambes.")

d1 = Drawing("Plan de la ville", "plan-epron.png")
d2 = Drawing("Epron de demain", "epron-futur.jpg")

try:
    session.add(i1)
    session.add(i2)
    session.add(i3)
    session.add(d1)
    session.add(d2)
    session.commit()
except Exception as e:
    session.rollback()
    print str(e)
