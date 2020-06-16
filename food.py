# Lint as: python3
"""Cuisine list."""

# pylint: disable=missing-class-docstring,invalid-name,pointless-statement,undefined-variable,non-ascii-name,too-few-public-methods

class Cuisine:

  class Breakfast:

    toasted_bread
    cacao
    cacao_poulain_grand_arome

    class Cereales:
      muesli
      granola_chocolat
      granola_fraise
      country_store
      miel_pops
      riz_soufflé
      corn_flakes

    class Confiture:
      prune
      fraise
      casis
      groseille
      abricot
      peche
      figues

      miel
      sirop_d_érable

    class Brunch:
      egg_benedicts
      hash_brown
      pancakes

  class Entrée:

    class BiscuitsSalés:
      belin
      tuc
      mini_pizza
      noix_de_cajou
      apericube
      wasabi_peas
      bhujia

    class Froide:
      tomate_mozzarella_balsamique
      avocat_balsamique
      pamplemousse
      melon
      melon_blanc
      cuncumber_balsamic
      pain_de_poisson  # (colin, concentrée de tomate)
      terrine_de_saumon
      carpaccio_de_boeuf
      radis_sel_beurre
      tuiles_au_parmesan_pavot

    class AmuseBouche:
      # Froid
      roulé_de_saumon_fumé
      # Chaud
      pruneaux_au_lard

    class Verinnes:
      saumon_avocat_fromage_frais
      noix_roqueford
      tomates_creme_feuille_balsamique
      poires_au_foie_gras

    class Dip:
      tapenade
      tzatziki
      guacamole
      humus
      tarama
      caviar
      oeuf_de_poissons
      oignon_dip
      saumon_fumé
      caviar_d_aubergines
      oeuf_de_cabillaud
      oeufs_de_lompe  # Black, read
      oeufs_de_saumon

      class Paté:
        liver
        mousse_de_canard
        foie_gras
        rillettes
        rillettes_de_thon
        rillettes_de_saumon
        terrine
        pate_en_croute

    class Chips:

      class PoatatoChips:
        vinegar
        mustard
        bbq

      tortilla_chips
      crispy_baked_vegetable_chips
      crevete
      toasted_bread
      blini
      gressins_aux_sesame  # pain fin

    class Chaude:
      nems
      pain_surprise
      boulette_de_fromage_pannée
      gougères_au_fromage
      accras_de_morue
      petit_fours
      mini_boudins

    class Friand:
      friand
      bouchée_à_la_reine  # / Vol-au-vent

      class Garniture:
        champinions
        fromage
        viande

  class Plat:

    class Soupes:
      avgolemono
      gazpacho
      gazpacho_cucumber
      gazpacho_poivrons
      tomate
      soupe_à_l_oignon
      lentilles
      lentilles_chorizo
      cheveux_d_anges
      poisson
      bouillon
      beef_chili

      croutons

    class Legumes:
      aubergines
      courgettes

      class Crudités:
        tomates
        concombre
        carottes
        choux_fleur
        radis

    class Feculents:

      class Riz:
        basmati
        thai
        risotto
        with_mix_brown

      blé
      croquettes_de_pomme_de_terre
      frites
      haricots_blancs
      haricots_verts
      nouilles_instantanées
      pates
      petit_pois
      polenta
      pommes_aux_four
      pommes_dauphine
      pommes_de_terre
      pommes_de_terre_sautées
      purée
      pâtes_fraiches
      rice_noodles
      rosti
      semoule
      spatzels
      vermicelles
      vermicelles_de_riz

    class Viande:
      chicken_blanc
      chicken_roti
      chicken_pannée
      fried_chicken
      schnitzel
      steak_haché
      steak_haché_oigions
      steak_haché_tomate
      viande_hachée
      cordon_bleu
      lardons
      bacon
      cannard
      escargot
      escaplope
      roti_de_boeuf  # (Boucherie auxerres)
      boulette_de_viande
      rognons

      class Saucisse:
        knacki
        chipolatas
        merguez
        boudin_blanc
        boudin_noir

      class Charcuterie:
        chorizo
        jambon
        sausisson
        salami
        pastrami

      class Animaux:
        agneau
        bison
        boeuf
        canard
        dinde
        chevreuille
        lapin
        pintade
        pork
        poulet
        sanglier

    class Poisson:
      oeuf_de_poisson
      poisson_panné
      thon
      rilletes_de_thon
      saumon
      saumon_fumé

      class FruitsDeMer:
        moules
        huitres
        coquille_saint_jacques
        crevettes
        surimi

    class Sauce:
      concentré_de_tomate
      tomate_sechées
      couli_de_tomate
      sauce_tomate
      sauce_tomate_basilic
      sauce_tomate_arrabiata
      sauce_bolognaise
      tomate_dentifrice
      carbonara
      creme_fraiche_concentré_tomate
      poivrons_cuits  # (+ ??)
      pulpe_de_tomate_oignons_ail
      sauce_curry
      sauce_soja_salé
      sauce_soja_sucré
      sauce_teriyaki
      sauce_cocktail
      moutarde_fine
      moutarde_graine
      moutarde_savora
      mayonnaise
      creme_fraiche_oignons_lardons
      peanut_coconut_sauce
      bechamel
      oignons_caramelisés
      sauce_forestiere

      sauce_chasseur  # (+ gelée de groseille)
      sauce_miel
      sauce_hollandaise

      # Sauce salades
      vinaigre_balsamic
      vinaigre_blanc
      vinaigre_de_xérès
      vinaigre_de_cidre
      vinaigre_de_riz
      mayonnaise

      class SauceViande:
        tartare
        bbq
        ketchup
        americaine
        blanche
        algerienne
        samourai
        bearnaise
        bordelaise
        bourguignonne
        poivre
        sauce_grand_veneur

      class Condimments:
        oignions_vinaigre
        mais_vinaigre
        cornichons_vinaigre

      class Ingrédients:
        lait_de_coco
        concentré_de_tomate
        bouillon_de_volailles
        champinions_de_paris

    class Épices:
      curry
      masala
      safran
      cumin
      paprika
      curcumin  # ~= turmeric
      herbes_de_provences
      ciboulettes
      basilic
      muscade

      graine_de_fenouilles
      échalote
      ail
      origan

    class Plat:
      blanquette_de_veau
      brioche_farci  # Quel est le nom exact ?
      burger
      cake
      cake_au_jambon
      carottes_fondantes_crème  # Recette maman
      carottes_caramélisées_au_miel
      champignons_farcis
      chanciau
      chili_con_carne
      choux_de_brussel_grillés
      club_sandwich
      confit_de_canard
      conserves_de_maquereau
      courges_chorizo  # Recette jeanne
      courgette_farcies
      croquette_de_pomme_de_terre_fourrée_fromage
      croquette_de_pomme_de_terre_fourrée_viande_hachée
      croziflette
      endives_aux_orange
      fallafel
      fondue_bourguignonne
      fondue_savoyarde
      fricassée_de_legumes_au_lardon
      fried_chicken
      gambas_coco_curry_à_l_ananas
      hachis_parmentier
      jambon_au_porto
      lasagne
      nouilles_instantanées

    class Vegetarien:
      aubergine_panée
      oeuf_à_la_coque
      poivrons_grillés
      ravioles
      raclette_francaise  # Fromage
      raclette_suisse
      risotto_aux_champignons
      soufflé
      tartine_miel_chèvre_chaud
      tomates_farcies_oeuf_fromage

    class Carne:
      magret_de_canard_miel
      paella
      poté_au_choux
      poulet_au_curry
      raviolis
      roti_de_porc_aux_ananas
      roti_de_porc_aux_pruneaux
      tartiflette
      tomates_farcies

    class SeaBased:
      moule_frites
      moule_frites_creme
      quenelles
      saumon_papillotes

    class FeuillesDeBricks:
      croustillant_de_chèvre
      thon

    class Gratin:
      gratin_dauphinois
      gratin_de_gnocchis
      gratin_de_ravioles
      gratin_de_pates
      gratin_de_quenelle
      gratin_de_poissons

    class Tarte:
      épinards
      quiche_lorraine
      quiche_aux_thon_tomate
      tourte
      tourte_aux_champinions
      tourte_aux_epinards
      tourte_aux_thon

    class Salades:
      caesar
      saumon_creme_fraiche
      ananas_avocat_crevette

      class Base:
        romaine
        mache
        frisé

      class Ingredients:
        germes_de_soja
        raisin

    class Crêpe:
      jambon_fromage
      lardons_fromage
      champinions_fromages

    class Pizza:
      oriental
      hawaienne
      savoyarde

    class Sandwitch:
      panini
      sandwich_suedois
      club_sandwitch
      sandwich_sous_marin
      wraps
      croque_monsieur_creme
      croque_monsieur_bechamel
      croissant_jambon_fromage

      class Kebab:
        tacos
        kebab
        faritas  # (chicken, maïs,...)

      class Garniture:
        saumon_creme_fraiche
        poulet_grillé_miel_fromage
        croque_baguette  # Baguette, viande haché, emental, oignon

      class Ingredients:
        paté
        charcuterie
        avocat
        crudités
        fromage
        herbes  # Basilique,...
        salade

    class Ingredients:
      pois_chiche
      champinions_de_paris
      cèpes
      germes_de_soja
      oignon_frits  # e.g. sushi
      wasabi

  class Fromage:
    cancoillotte
    kiri
    vache_qui_rit
    boursin
    boursin_aux_noix
    philadelphia
    buche_de_chevre
    emmental
    camembert
    chaussée_aux_moines
    fromage_ail_et_fines_herbes
    cervelle_de_canut
    tranche_cheddar
    tranche_fromage_special_croque_monsieur
    caprice_des_dieux

    class Raclette:
      nature
      poivre
      fumé

  class Pain:
    pain_campagnard
    pain_de_seigle
    pain_au_pavot
    pain_suedois  # Sandwitch
    petit_pain_suedois
    baguette
    baguette_moulée
    baguette_tradition
    baguette_en_epis  # Forme
    pain_de_mie
    craquottes
    biscottes
    pain_noir  # Allemand
    pain_avec_raisins
    pain_avec_noix

  class Desert:

    class Desert:
      desert_oriental_maman  # (sorte de soupe avec pruneaux,...)
      bananes_flambées
      pommes_caramelisés
      pommes_sur_du_pain  # Recette maman
      pain_perdu
      glace  # cône, boulle
      sorbet
      chè_đỗ_đen_hạt_sen  # Soupe vietnamienne tapioca, gingenbre
      poire_belle_helene
      panna_cotta
      crème_brûlée
      chataigne_grillés
      marron_glacé
      soupe_chinoise  # (recette Benoît)
      bugnes
      beignet
      pain_d_epice
      ananas_frit  # Frits
      riz_au_lait

    class Fruits:
      brugnon
      nectarine
      peches
      abricots
      bananes
      raisins  # (blanc, noir)
      cerises
      pommes
      poire
      pasteque
      ananas

      class FruitRouges:
        cassis
        groseilles
        framboise
        mûre
        myrtille
        sureau
        fraise
        fraise_des_bois

    class Gateau:
      tiramisu
      fondant_au_chocolat
      chocolat
      charlotte_aux_fruits
      tarte_tatin
      clafouti
      cheese_cake
      crumble
      profiteroles
      vacherin
      gâteux_aux_ananas
      gâteaux_aux_amandes
      galette_des_rois
      cake_cappuccino  # petit beurres trempés dans café et recouvert de chocola
      flan_pomme_caramel

    class Tartes:
      tarte_tatin
      tarte_citron_meringué
      tarte_aux_prunes
      tarte_frangipane_abricot
      tarte_frangipane_poire

    class Bonbon:
      loucum
      arlequin
      têtes_brulées
      haribo
      haribo_coca_cola
      haribo_schtroumpf
      haribo_dragibus
      haribo_gummy_bear
      haribo_croqodile
      fraise_tagada
      kinder_bueno
      kinder_surprise
      kitkat
      mars

    class Pâtisserie:
      opera
      religieuse
      paris_brest
      mille_feuille
      éclair  # chocolat, caffé
      tartelettes_aux_fruits
      meringues
      choux_a_la_creme

      class Macarons:
        lavende
        café
        mangue
        caramel_beurre_salé
        chocolat
        pistache
        vanille

    class Laitages:
      compote_de_pommes
      compote_de_pommes_chataigne
      danette_caffe
      danette_caramel
      danette_chocolat
      mousse_au_chocolat
      mousse_au_caffe
      mousse_au_citron
      mousse_au_marrons
      mousse_au_speculoos
      laitière
      crème_de_marrons
      petit_suisses
      yaourt_blanc
      yaourt_greque
      fromage_blanc
      yaourt_citron
      yaourt_vanille
      yaourt_fruits_mixées
      flan_caramel
      petit_filous

      class YaourtGarniture:
        miel
        sucre  # blanc, roux,...
        petit_ecolier
        confiture

    class Vienoiseries:
      brioche
      croissant
      baguette_viennoise
      pain_au_lait
      pain_au_chocolat
      pain_aux_raisins

    class Biscuits:
      petit_ecolier  # (lait, 45%, 70%)
      digestive_lu
      granola_lu
      biscuits_petit_beurre_lu
      kinders
      fererro
      mikado
      langue_de_chat
      cigarettes_russes
      biscuit_cuillere
      macaron_noix_de_coco
      biscuit_figue
      tartelette_biscuit
      madeleine
      finger_chocolat
      paille_d_or  # Framboise
      oreo
      delichoc
      pepito
      delacre_sprits
      delacre_assortiment_tea_time
      speculoos

    class Chocolat:
      chocolat_poulain
      crunch
      ferrero_rocher
      chocolat_noisettes
      chocolat_fourré
      nutella

    class Crêpes:
      suzette
      pommes_confites
      flambée

    class Verrines:
      citron_meringué
      fraises_speculoos_yaourt

    class Ingredients:
      sucre
      sucre_glace
      cassonade
      confetti
      mascarpone
      pâte_brisée
      pâte_feuilletée
      pâte_sablée
      raisins_sec
      amandes_en_poudre
      amandes_concassées

  class Boisson:

    class Soft:
      jus_de_tomate
      jus_d_abricot
      jus_de_pomme
      jus_d_annanas
      jus_de_pamplemousse
      jus_multifruit
      jus_de_citron
      jus_de_guyave
      sirop_monin
      sirop_monin_fruit_de_la_passion
      pulco_citron
      smoothie

      yaourt_a_boire_yop
      yaourt_a_boire_danactive

    class Soda:
      pepsi
      sprite
      ice_tea
      orangina
      san_pellegrino_agrumes

    class CafféThé:
      thé
      thé_indien  # Lait, sucre
      thé_chai
      tisane  # Citron
      caffé
      ice_coffé
      dalgona_coffee
      capucino

    class Alcholic:
      bierre_ipa
      bierre_blonde
      bierre_blanche
      bierre_brune
      bierre_fruité
      cidre
      cidre_d_ananas
      vin_blanc
      vin_rose
      vin_rouge
      champagne
      planteur

      class Chaud:
        apple_cider
        vin_chaud


class World:

  class Europe:

    class France:
      coq_au_vin
      boeuf_bourguignon

      class FastFood:
        tacos
        mac_donald

    class Italian:
      piccata  # veal, chicken

    class GreatBritain:
      fish_and_chips
      chicken_pot_pie

    class Germany:
      spreewaldgurken
      schnitzel
      choucroute_garnie
      bretzels

    class Grece:
      avgolemono
      moussaka

    class Spain:
      gazpacho
      paella

    class Suisse:

      class FastFood:
        holy_cow

  class Oriental:

    class Maroc:
      pain_farcis
      couscous
      tagine

      patisseries_orientales

    class Libanese:
      falafels
      dolmas

    class Turkey:
      pass

  class Ameriques:

    class American:
      # Starters
      garlic_fries
      chili_fries
      oignon_rings
      avocado_toast

      # Brunch
      hash_brown
      eggs_benedict
      saucisses  # petites saucisse breakfast
      flageolets_beans  # haricots blancs avec sauce tomate sucrée

      phili_cheesesteak

      cheesesteak
      gumbo_soup

      zuchini_bread
      banana_bread

      class FastFood:
        katsu_burger

    class Canadian:
      poutine

  class Asia:

    class Japan:
      onigiri
      gyoza
      takoyaki
      sushi
      ramen
      okonomiyaki
      chicken_katzu_curry
      pork_katzu
      pork_don
      katsudon
      gari  # gingembre confit

      sauce_teriaki

    class Chineese:
      pork_au_caramel
      canard_laqué
      rouleaux_de_printemps
      dumplings

      sauce_fish
      sauce_aigre_douce

      fried_mochi_ball
      fried_pinapple

    class Thai:
      yellow_curry  # green, red

    class Vietnamian:
      nems
      bánh_mì
      chè_đỗ_đen

    class Indian:
      samosa
      chiken_tikka_masala
      butter_chicken
      paneer
      achaar  # Indian pickle

    class Korean:
      korean_fried_chicken


class Ustensile:

  class Recipient:
    casserole
    poêle
    plat_a_tarte
    plat_a_gratin
    plat_a_cake
    moule_souples
    saladier
    verrines
    bol
    assiette
    assiette_a_soupe
    coquetier
    verre
    tupperware

  class Outil:
    couteaux_de_cuisine
    cuillere_en_bois
    louche
    eplucheur
    rape  # Fromage, rosti,...
    spatule
    maryse  # spatule en silicone
    fouet
    pince  # e.g. pour friture
    pinceau  # pour badigeonner
    mortier  # ecraseur (guacamole, pomme de terre)
    rouleau_a_patisserie
    ouvre_boite
    decapsuleur
    tire_bouchon
    passoire
    pressoir
    presse_purée  # ?

  aluminium
  film_transparent
  papier_sulfurisé
  sachet_fermeture_zip  # pochette plastique
  papier_absorbant

  nappe_de_bambou  # Sushi
  bouchon

  éponge
  liquide_vaisselle

  mixeur
  batteur  # Blanc en neige
  planche_bois_a_decouper
  planche_a_pain
  appareil_a_crepe
  appareil_a_raclette  # Suisse / France model
  appareil_a_fondue
  moule_a_gauffre
  presse_a_panini
  plancha
  four
  micro_onde
  refrigirateur
  congelateur
  grille_pain
  boilloire
  machine_a_café
  egouteur_a_salade
