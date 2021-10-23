import re


# calculate number of ingredients for each dish
def No_of_ings(x):
    s0 = []
    count=0
    for ing in x:
        count += 1
    return(count)

###############################################

# Change list of ingredients into a string before applying vectorization
# clean up the ingredients list

def list_of_ing(x):
    s0 = []
    count=0

    for ing in x:
        ing = ing.lower()

        ing=re.sub(r'\bbertolli®\b', '', ing.lower())
        ing=re.sub(r"\bhellmann's®\b", '', ing.lower())
        ing=re.sub(r"\bpaso™\b", '', ing.lower())
        ing=re.sub(r"\bbacardi®\b", '', ing.lower())
        ing=re.sub(r"\bi can't believe it's not butter!®\b", '', ing.lower())
        ing=re.sub(r"\bgold®\b", '', ing.lower())
        ing=re.sub(r"\bknorr®\b", '', ing.lower())
        ing=re.sub(r"\bjohnsonville®\b", '', ing.lower())
        ing=re.sub(r"\bhellmannâ€™ or best food canola cholesterol free\b", '', ing.lower())
        ing=re.sub(r"\bsides™\b", '', ing.lower())
        ing=re.sub(r"\bpillsbury™\b", '', ing.lower())
        ing=re.sub(r"\bsargento®\b", '', ing.lower())
        ing=re.sub(r"\bcrock®\b", '', ing.lower())
        ing=re.sub(r"\boreo®\b", '', ing.lower())
        ing=re.sub(r"\bmccormick®\b", '', ing.lower())
        ing=re.sub(r"\bvalley®\b", '', ing.lower())
        ing=re.sub(r"\branch®\b", '', ing.lower())
        ing=re.sub(r"\bfoods®\b", '', ing.lower())
        ing=re.sub(r"\bfarms®\b", '', ing.lower())
        ing=re.sub(r"\bcrocker™\b", '', ing.lower())
        ing=re.sub(r"\byoplait®\b", '', ing.lower())
        ing=re.sub(r"\bvalley®\b", '', ing.lower())
        ing=re.sub(r"\bsalad®\b", '', ing.lower())
        ing=re.sub(r"\bsides™\b", '', ing.lower())
        ing=re.sub(r"\blakes®\b", '', ing.lower())
        ing=re.sub(r"\bmazola®\b", '', ing.lower())
        ing=re.sub(r"\blipton®\b", '', ing.lower())
        ing=re.sub(r"\bsecrets®\b", '', ing.lower())
        ing=re.sub(r"\bsargento®\b", '', ing.lower())
        ing=re.sub(r"\bpanetini®\b", '', ing.lower())
        ing=re.sub(r"\bragu®\b", '', ing.lower())
        ing=re.sub(r"\brobusto!®\b", '', ing.lower())
        ing=re.sub(r"\bfrank's®\b", '', ing.lower())
        ing=re.sub(r"\bredhot®\b", '', ing.lower())
        ing=re.sub(r"\bbreyers®\b", '', ing.lower())
        ing=re.sub(r"\bcrystal®\b", '', ing.lower())
        ing=re.sub(r"\bvay®\b", '', ing.lower())
        ing=re.sub(r"\bteriyaki®\b", 'teriyaki', ing.lower())
        ing=re.sub(r"\btabasco®\b", 'tabasco', ing.lower())
        ing=re.sub(r"\btruvía®\b", '', ing.lower())
        ing=re.sub(r"\bblends®\b", '', ing.lower())
        ing=re.sub(r"\bwish-bone®\b", '', ing.lower())
        ing=re.sub(r"\bbest®\b", '', ing.lower())
        ing=re.sub(r"\bislands®\b", '', ing.lower())
        ing=re.sub(r"\bbell®\b", '', ing.lower())
        ing=re.sub(r"\b&\b", 'and', ing.lower())
        ing=re.sub(r"\bwhite®\b", '', ing.lower())
        ing=re.sub(r"\bbow-tie pasta\b", '', ing.lower())
        ing=re.sub('wish bone', '', ing.lower())
        ing=re.sub('aleppo pepper', 'aleppo_pepper', ing.lower())
        ing=re.sub('chile de arbol', 'chile_de_arbol', ing.lower())

        ing=re.sub('italian seasoning', 'italian_seasoning', ing.lower())
        ing=re.sub('cajun seasoning', 'cajun_seasoning', ing.lower())
        ing=re.sub('creole style seasoning', 'creole_seasoning', ing.lower())
        ing=re.sub('creole seasoning', 'creole_seasoning', ing.lower())
        ing=re.sub('old bay seasoning', 'old_bay_seasoning', ing.lower())
        ing=re.sub('taco seasoning', 'taco_seasoning', ing.lower())
        ing=re.sub('mexican seasoning', 'taco_seasoning', ing.lower())
        ing=re.sub('boil seasoning', 'boil_seasoning', ing.lower())
        ing=re.sub('seafood seasoning', 'seafood_seasoning', ing.lower())
        ing=re.sub('greek seasoning', 'greek_seasoning', ing.lower())
        ing=re.sub('poultry seasoning', 'poultry_seasoning', ing.lower())
        ing=re.sub('garlic pepper seasoning', 'garlic_pepper_seasoning', ing.lower())
        ing=re.sub('jerk pepper seasoning', 'jerk_seasoning', ing.lower())
        ing=re.sub('bbq sauce', 'bbq_sauce', ing.lower())
        ing=re.sub('all purpose seasoning', 'all_purpose_seasoning', ing.lower())
        ing=re.sub('salad seasoning', 'salad_seasoning', ing.lower())
        ing=re.sub('chili seasoning', 'chili_seasoning', ing.lower())
        ing=re.sub('pork seasoning', 'pork_seasoning', ing.lower())
        ing=re.sub('tex mex seasoning', 'taco_seasoning', ing.lower())
        ing=re.sub('beau monde seasoning', 'beau_monde_seasoning', ing.lower())
        ing=re.sub('spike seasoning', 'spike_seasoning', ing.lower())
        ing=re.sub('herb seasoning', 'herb_seasoning', ing.lower())
        ing=re.sub('vegetable seasoning', 'vegetable_seasoning', ing.lower())
        ing=re.sub('salad seasoning', 'salad_seasoning', ing.lower())
        ing=re.sub('lemon pepper seasoning', 'lemon_pepper_seasoning', ing.lower())
        ing=re.sub('tandoori seasoning', 'tandoori_seasoning', ing.lower())
        ing=re.sub('adobo seasoning', 'adobo_seasoning', ing.lower())
        ing=re.sub('grill seasoning', 'grill_seasoning', ing.lower())
        ing=re.sub('sazon seasoning', 'sazon_seasoning', ing.lower())
        ing=re.sub('accent seasoning', 'accent_seasoning', ing.lower())
        ing=re.sub('ground black pepper', 'black_pepper', ing.lower())
        ing=re.sub(r'\bblack pepper\b', 'black_pepper', ing.lower())
        ing=re.sub('fajita seasoning', 'fajita_seasoning', ing.lower())
        ing=re.sub('lamb seasoning', 'lamb_seasoning', ing.lower())
        ing=re.sub('spaghetti sauce seasoning', 'spaghetti_sauce_seasoning', ing.lower())
        ing=re.sub('barbecue seasoning', 'barbecue_seasoning', ing.lower())
        ing=re.sub('vegeta seasoning', 'vegeta_seasoning', ing.lower())
        ing=re.sub('steak seasoning', 'steak_seasoning', ing.lower())
        ing=re.sub('maple syrup', 'maple_syrup', ing.lower())
        ing=re.sub('granny smith apples', 'granny_smith_apples', ing.lower())
        ing=re.sub('cottage cheese', 'cottage_cheese', ing.lower())
        ing=re.sub('refried beans', 'refried_beans', ing.lower())
        ing=re.sub('chilli paste', 'chilli_paste', ing.lower())
        ing=re.sub('pak choi', 'pak_choi', ing.lower())
        ing=re.sub('pan drippings', 'pan_drippings', ing.lower())
        ing=re.sub('pasilla chiles', 'pasilla_chiles', ing.lower())
        ing=re.sub(r"\bpasilla\b", 'pasilla_chiles', ing.lower())
        ing=re.sub('pasilla pepper', 'pasilla_pepper', ing.lower())
        ing=re.sub('mulato chiles', 'mulato_chiles', ing.lower())
        ing=re.sub('pickle juice', 'pickle_juice', ing.lower())
        ing=re.sub('pickle relish', 'pickle_relish', ing.lower())
        ing=re.sub('pickle juice', 'pickle_juice', ing.lower())
        ing=re.sub('jalapeno peppers', 'jalapeno', ing.lower())
        ing=re.sub('dill pickles', 'dill_pickles', ing.lower())
        ing=re.sub('pickled vegetables', 'pickled_vegetables', ing.lower())
        ing=re.sub('sweet pickle', 'sweet_pickle', ing.lower())
        ing=re.sub('pickled beets', 'pickled_beets', ing.lower())
        ing=re.sub('pickled okra', 'pickled_okra', ing.lower())
        ing=re.sub('pickled carrots', 'pickled_carrots', ing.lower())
        ing=re.sub('pinot noir', 'pinot_noir', ing.lower())
        ing=re.sub('pinot blanc', 'pinot_blanc', ing.lower())
        ing=re.sub('chile de arbol', 'arbol', ing.lower())
        ing=re.sub('balsamic vinegar', 'balsamic', ing.lower())
        ing=re.sub('bamboo shoots', 'bamboo', ing.lower())
        ing=re.sub('pure acai puree', 'acai_puree', ing.lower())
        ing=re.sub('paste', '', ing.lower())
        ing=re.sub('acorn squash', 'acorn_squash', ing.lower())
        ing=re.sub('apple cider vinegar', 'apple_cider', ing.lower())
        ing=re.sub('applesauce', '', ing.lower())
        ing=re.sub('applewood', '', ing.lower())
        ing=re.sub('barbecued', 'barbecue', ing.lower())
        ing=re.sub('bell pepper', 'bell_pepper', ing.lower())
        ing=re.sub('blackberry', '', ing.lower())
        ing=re.sub('blueberry', '', ing.lower())
        ing=re.sub('brioche bread', 'brioche', ing.lower())
        ing=re.sub('cannellini beans', 'cannellini', ing.lower())
        ing=re.sub('cannellini bean', 'cannellini', ing.lower())
        ing=re.sub('caraway seeds', 'caraway', ing.lower())
        ing=re.sub('caraway seed', 'caraway', ing.lower())
        ing=re.sub('cassava root flour', 'cassava', ing.lower())
        ing=re.sub('champagne vinegar', 'champagne_vinegar', ing.lower())
        ing=re.sub('chana dal', 'chana_dal', ing.lower())
        ing=re.sub('char siu', 'char_siu', ing.lower())
        ing=re.sub('cheddar cheese', 'cheddar', ing.lower())
        ing=re.sub('chinese chives', 'chives', ing.lower())
        ing=re.sub('chinkiang vinegar', 'chinkiang', ing.lower())
        ing=re.sub('bok choy', 'bok_choy', ing.lower())
        ing=re.sub('beef consomme', 'beef_consomme', ing.lower())
        ing=re.sub('crimini mushrooms', 'crimini', ing.lower())
        ing=re.sub('demi-glace', 'demi_glace', ing.lower())
        ing=re.sub('fava beans', 'fava', ing.lower())
        ing=re.sub('fava bean', 'fava', ing.lower())
        ing=re.sub('feta cheese', 'feta', ing.lower())
        ing=re.sub('foie gras', 'foie_gras', ing.lower())
        ing=re.sub('chees fresco queso', 'fresco_queso', ing.lower())
        ing=re.sub('fresco queso', 'fresco_queso', ing.lower())
        ing=re.sub('queso fresco', 'fresco_queso', ing.lower())
        ing=re.sub('gai lan', 'gai_lan', ing.lower())
        ing=re.sub('garam masala', 'masala', ing.lower())
        ing=re.sub('garbanzo beans', 'garbanzo', ing.lower())
        ing=re.sub('garbanzo bean', 'garbanzo', ing.lower())
        ing=re.sub('bouquet garni', 'bouquet_garni', ing.lower())
        ing=re.sub('gruyere cheese', 'gruyere', ing.lower())
        ing=re.sub('guajillo chiles', 'chili', ing.lower())
        ing=re.sub('guajillo', 'chili', ing.lower())
        ing=re.sub('masa harina', 'masa_harina', ing.lower())
        ing=re.sub('shahi jeera', 'shahi_jeera', ing.lower())
        ing=re.sub('kasuri methi', 'kasuri_methi', ing.lower())
        ing=re.sub('kecap manis', 'kecap_manis', ing.lower())
        ing=re.sub('dashi kombu', 'dashi_kombu', ing.lower())
        ing=re.sub('maida flour', 'maida_flour', ing.lower())
        ing=re.sub('manchego cheese', 'manchego_cheese', ing.lower())
        ing=re.sub('nigella seeds', 'nigella', ing.lower())
        ing=re.sub('nigella seed', 'nigella', ing.lower())
        ing=re.sub('sesame seed', 'nigella', ing.lower())
        ing=re.sub('sesame seed', 'nigella', ing.lower())
        ing=re.sub('sesame oil', 'oil', ing.lower())
        ing=re.sub('pecorino cheese', 'pecorino', ing.lower())
        ing=re.sub('pecorino romano cheese', 'pecorino', ing.lower())
        ing=re.sub('picholine olives', 'olive', ing.lower())
        ing=re.sub('picholine olive', 'olive', ing.lower())
        ing=re.sub('pomegranate seeds', 'pomegranate_seeds', ing.lower())
        ing=re.sub('pomegranate', 'pomegranate_seeds', ing.lower())
        ing=re.sub('pomegranate molasses', 'pomegranate_molasses', ing.lower())
        ing=re.sub('poppy seeds', 'poppy_seeds', ing.lower())
        ing=re.sub('poppy seed', 'poppy_seeds', ing.lower())
        ing=re.sub('poppyseeds', 'poppy_seeds', ing.lower())
        ing=re.sub('porcini mushrooms', 'porcini', ing.lower())
        ing=re.sub('pork loin', 'pork', ing.lower())
        ing=re.sub('herbes de provence', 'herbes_de_provence', ing.lower())
        ing=re.sub('provolone cheese', 'provolone', ing.lower())
        ing=re.sub('rapeseed oil', 'rapeseed', ing.lower())
        ing=re.sub('raspberry preserves', 'raspberry_preserves', ing.lower())
        ing=re.sub('raspberry preserve', 'raspberry_preserves', ing.lower())
        ing=re.sub('raspberry jam', 'raspberry_preserves', ing.lower())
        ing=re.sub('pickle relish', 'pickle_relish', ing.lower())
        ing=re.sub('roquefort cheese', 'roquefort', ing.lower())
        ing=re.sub('rose petals', 'rose_petals', ing.lower())
        ing=re.sub('rotisserie chicken', 'rotisserie_chicken', ing.lower())
        ing=re.sub('sambal ulek', 'sambal_ulek', ing.lower())
        ing=re.sub('shichimi togarashi', 'shichimi_togarashi', ing.lower())
        ing=re.sub('shiitake mushrooms', 'shiitake', ing.lower())
        ing=re.sub('shiitake mushroom', 'shiitake', ing.lower())
        ing=re.sub('portobello mushrooms', 'shiitake', ing.lower())
        ing=re.sub('portobello mushroom', 'shiitake', ing.lower())
        ing=re.sub('sichuanese chili', 'sichuanese', ing.lower())
        ing=re.sub('sichuanese pepper', 'sichuanese', ing.lower())
        ing=re.sub('soba noodles', 'soba', ing.lower())
        ing=re.sub('spelt flour', 'spelt', ing.lower())
        ing=re.sub('stilton cheese', 'stilton', ing.lower())
        ing=re.sub('szechwan peppercorns', 'szechwan_peppercorns', ing.lower())
        ing=re.sub('toor dal', 'toor_dal', ing.lower())
        ing=re.sub('urad dal', 'urad_dal', ing.lower())
        ing=re.sub('haricots verts', 'haricots_verts', ing.lower())
        ing=re.sub('wish bone', '', ing.lower())
        ing=re.sub('bengal gram', 'bengal_gram', ing.lower())
        ing=re.sub('queso blanco', 'queso_blanco', ing.lower())
        ing=re.sub('lily buds', 'lily_buds', ing.lower())
        ing=re.sub('lily bud', 'lily_buds', ing.lower())
        ing=re.sub('channa dal', 'channa_dal', ing.lower())
        ing=re.sub('chat masala', 'chat_masala', ing.lower())
        ing=re.sub('chihuahua cheese', 'chihuahua', ing.lower())
        ing=re.sub('corn-on-the-cob', 'corn', ing.lower())
        ing=re.sub('flounder', 'fish', ing.lower())
        ing=re.sub('garbanzo beans', 'garbanzo', ing.lower())
        ing=re.sub('garbanzo bean', 'garbanzo', ing.lower())
        ing=re.sub('kaiser rolls', 'kaiser_rolls', ing.lower())
        ing=re.sub('kaiser roll', 'kaiser_rolls', ing.lower())
        ing=re.sub('macadamia nuts', 'macadamia', ing.lower())
        ing=re.sub('monkfish', 'fish', ing.lower())
        ing=re.sub('passion fruit', 'passion_fruit', ing.lower())
        ing=re.sub('picante sauce', 'picante_sauce', ing.lower())
        ing=re.sub('romano cheese', 'romano', ing.lower())
        ing=re.sub('peach schnapps', 'schnapps', ing.lower())
        ing=re.sub('apple schnapps', 'schnapps', ing.lower())
        ing=re.sub('peppermint schnapps', 'schnapps', ing.lower())
        ing=re.sub('sponge cake', 'sponge_cake', ing.lower())
        ing=re.sub('sponge', 'sponge_cake', ing.lower())
        ing=re.sub('muenster cheese', 'muenster', ing.lower())
        ing=re.sub(' chiles', 'mulato', ing.lower())
        ing=re.sub('teriyaki marinade', 'teriyaki', ing.lower())
        ing=re.sub('soy marinade', 'soy', ing.lower())
        ing=re.sub('jerk marinade', 'jerk', ing.lower())
        ing=re.sub('orange marmalade', 'marmalade', ing.lower())
        ing=re.sub('grand marnier', 'grand_marnier', ing.lower())
        ing=re.sub('gran marnier', 'grand_marnier', ing.lower())
        ing=re.sub(r'\bthigh\b', 'chicken', ing.lower())
        ing=re.sub('thigh', 'chicken', ing.lower())



    
        ing=re.sub(r"\blinguini\b", 'pasta', ing.lower())
        ing=re.sub(r"\btagliatelle\b", 'pasta', ing.lower())
        ing=re.sub(r"\bpenne\b", 'pasta', ing.lower())
        ing=re.sub(r'\blasagne\b', 'pasta', ing.lower()) 
        ing=re.sub(r'\bstrozzapreti\b', 'pasta', ing.lower()) 
        ing=re.sub(r'\btortellini\b', 'pasta', ing.lower()) 
        ing=re.sub(r'\bbigoli\b', 'pasta', ing.lower()) 
        ing=re.sub(r'\bpappardelle\b', 'pasta', ing.lower()) 
        ing=re.sub(r'\bmacaroni\b', 'pasta', ing.lower()) 
        ing=re.sub(r'\bmostaccioli\b', 'pasta', ing.lower()) 
        ing=re.sub(r'\brotini\b', 'pasta', ing.lower())
        ing=re.sub(r'\brigatoni\b', 'pasta', ing.lower())
        ing=re.sub(r'\btortellini\b', 'pasta', ing.lower())
        ing=re.sub(r'\btortellini\b', 'pasta', ing.lower())
        ing=re.sub(r'\bfettuccine\b', 'pasta', ing.lower())
        ing=re.sub(r'\bspaghetti\b', 'pasta', ing.lower())
        ing=re.sub(r'\blasagne\b', 'pasta', ing.lower())
        ing=re.sub(r'\borecchiette\b', 'pasta', ing.lower())
        ing=re.sub(r'\bspaghettini\b', 'pasta', ing.lower())
        ing=re.sub(r'\borzo\b', 'pasta', ing.lower())
        ing=re.sub(r'\brigatoni\b', 'pasta', ing.lower())
        ing=re.sub(r'\bpastina\b', 'pasta', ing.lower())
        ing=re.sub(r'\bcannelloni\b', 'pasta', ing.lower())
        ing=re.sub(r'\btubetti\b', 'pasta', ing.lower())
        ing=re.sub(r'\bcavatelli\b', 'pasta', ing.lower())
        ing=re.sub(r'\bbucatini\b', 'pasta', ing.lower())
        ing=re.sub(r'\bpiccolini\b', 'pasta', ing.lower())
        ing=re.sub(r'\bmacaroni\b', 'pasta', ing.lower())
        ing=re.sub(r'\bspaghetti\b', 'pasta', ing.lower())
        ing=re.sub(r'\bpepe\b', 'pasta', ing.lower())
        ing=re.sub(r'\brotini\b', 'pasta', ing.lower())
        ing=re.sub('lasagna', 'pasta', ing.lower())
        ing=re.sub('linguine', 'pasta', ing.lower())
        ing=re.sub('fettucine', 'pasta', ing.lower())
        ing=re.sub('angel hair', 'pasta', ing.lower())
        ing=re.sub('angel hairs', 'pasta', ing.lower())
        ing=re.sub('fusilli', 'pasta', ing.lower())
        ing=re.sub('ravioli', 'pasta', ing.lower())
        ing=re.sub('ditalini', 'pasta', ing.lower())
        ing=re.sub('manicotti', 'pasta', ing.lower())
        ing=re.sub('rigate', 'pasta', ing.lower())
        ing=re.sub('rotelle', 'pasta', ing.lower())


        ing=re.sub(r'\bchilies\b', 'chili', ing.lower())
        ing=re.sub(r'\bchile\b', 'chili', ing.lower())
        ing=re.sub('chile', 'chili', ing.lower())
        ing=re.sub('chilli', 'chili', ing.lower())  

        ing=re.sub(r'\btumeric\b', 'turmeric', ing.lower())
        ing=re.sub(r'\byolk\b', 'egg', ing.lower())
        ing=re.sub(r'\ballspice\b', 'spice', ing.lower())
        ing=re.sub(r'\bbeansprouts\b', 'sprout', ing.lower())
        ing=re.sub(r'\bdijon\b', 'mustard', ing.lower())
    #    ing=re.sub(r'\bpeppercorn\b', 'pepper', ing.lower())
     #   ing=re.sub('peppercorn', 'pepper', ing.lower())    
        ing=re.sub(r'\bsprig\b', 'spring', ing.lower())
        ing=re.sub('sprig', 'spring', ing.lower())
        ing=re.sub('ancho', 'anchovy', ing.lower())    
        ing=re.sub('andouille', 'sausage', ing.lower())
        ing=re.sub('bok choy', 'bok_choy', ing.lower())
        ing=re.sub(r'\bcreme\b', 'cream', ing.lower())
        ing=re.sub('creme', 'cream', ing.lower())
        ing=re.sub('fivespice', 'spice', ing.lower())
        ing=re.sub('pinto beans', 'pinto', ing.lower())
        ing=re.sub('pinto bean', 'pinto', ing.lower())
        ing=re.sub('salmon', 'fish', ing.lower()) 
        ing=re.sub('yolk', 'egg', ing.lower()) 
        ing=re.sub('anchovyvy', 'anchovy', ing.lower())
        ing=re.sub('baking soda', 'baking_soda', ing.lower())
        ing=re.sub('fivespice', 'spice', ing.lower())
        ing=re.sub('mayonaise', 'mayonnaise', ing.lower())
        ing=re.sub('mayonnais', 'mayonnaise', ing.lower())
        ing=re.sub('mayonnaisee', 'mayonnaise', ing.lower())
        ing=re.sub('yoghurt', 'yogurt', ing.lower())
        ing=re.sub('bbq', 'barbecue', ing.lower())
        ing = re.sub(r'[^\w\s]','',ing) 
        ing=re.sub(r'\bcreme\b', 'cream', ing.lower())
        ing=re.sub('creme', 'cream', ing.lower())
        ing=re.sub('fivespice', 'spice', ing.lower())
        ing=re.sub('chilies', 'chili', ing.lower())
        ing=re.sub('chees', 'cheese', ing.lower())
        ing=re.sub('cheesee', 'cheese', ing.lower())
        ing=re.sub('marsala', 'wine', ing.lower())
        ing=re.sub('bonito', 'fish', ing.lower())
        ing=re.sub('salmon', 'fish', ing.lower())
        ing=re.sub('cod', 'fish', ing.lower())
        ing=re.sub('cornmeal', 'cornflour', ing.lower())
        ing=re.sub('crabmeat', 'crab', ing.lower())
        ing=re.sub('drumstick', 'ice_cream', ing.lower())
        ing=re.sub('ice cream', 'ice_cream', ing.lower())
        ing=re.sub('halibut', 'fish', ing.lower())
        ing=re.sub('snapper', 'fish', ing.lower())
        ing=re.sub('bass', 'fish', ing.lower())
        ing=re.sub('bell pepper', 'bell_pepper', ing.lower())
        ing=re.sub('herbes', 'herb', ing.lower())
        ing=re.sub('mahimahi', 'fish', ing.lower())
        ing=re.sub('tuna', 'fish', ing.lower())
        ing=re.sub('mahi', 'fish', ing.lower())
        ing=re.sub('slaw', 'coleslaw', ing.lower())
        ing=re.sub('anchovyvies', 'anchovy', ing.lower())
        ing=re.sub('artichok', 'artichoke', ing.lower())
        ing=re.sub('asafetida', 'asafoetida', ing.lower())
        ing=re.sub('pico de gallo', 'pico_de_gallo', ing.lower())
        ing=re.sub('grits', 'grit', ing.lower())
        ing=re.sub('mashed potatoes', 'mashed_potatoes', ing.lower())
        ing=re.sub('parmigianoreggiano', 'parmigiano', ing.lower())
#        ing=re.sub('vinaigrette', 'vinegar', ing.lower())
        ing=re.sub('whitefish', 'fish', ing.lower())
        ing=re.sub('wholemilk', 'milk', ing.lower())
        ing=re.sub('artichokee', 'artichoke', ing.lower())
        ing=re.sub('artichokees', 'artichoke', ing.lower())
        ing=re.sub('lemon grass', 'lemongrass', ing.lower())
        ing=re.sub('ras el hanout', 'ras_el_hanout', ing.lower())
        ing=re.sub('hellmann', '', ing.lower())
        ing=re.sub('kraft', '', ing.lower())
        ing=re.sub('sauc', 'sauce', ing.lower())
        ing=re.sub('won ton', 'wonton', ing.lower())
        ing=re.sub('colecoleslaw', 'coleslaw', ing.lower())
        ing=re.sub('dillweed', 'dill', ing.lower())
        ing=re.sub('hot dog', 'hot_dog', ing.lower())
        ing=re.sub('hot dog bun', 'bun', ing.lower())
        ing=re.sub('hot dogs', 'hot_dogs', ing.lower())
        ing=re.sub('hens', 'chicken', ing.lower())
        ing=re.sub('hen', 'chicken', ing.lower())
        ing=re.sub('watermelon', 'melon', ing.lower())
        ing=re.sub('saucee', 'sauce', ing.lower())
        ing=re.sub('saucees', 'sauce', ing.lower())
        ing=re.sub('spring roll', 'spring_roll', ing.lower())
        ing=re.sub('corned beef', 'corned_beef', ing.lower())
        ing=re.sub('key lime', 'key_lime', ing.lower())
        ing=re.sub('mung beans', 'mung_beans', ing.lower())
        ing=re.sub('mung bean', 'mung_beans', ing.lower())
        ing=re.sub('lo mein', 'lo_mein', ing.lower())
        ing=re.sub('chow mein', 'chow_mein', ing.lower())
        ing=re.sub('rose water', 'rose_water', ing.lower())
        ing=re.sub(r'\brose water\b', 'rose_water', ing.lower())
        ing=re.sub('cream cheese', 'cream_cheese', ing.lower())
        ing=re.sub('sour cream', 'sour_cream', ing.lower())
        ing=re.sub('swordfish', 'fish', ing.lower())
        ing=re.sub('veggie', 'vegetable', ing.lower())
        ing=re.sub('broccolini', 'broccoli', ing.lower())
        ing=re.sub('cantaloupe', 'melon', ing.lower())
        ing=re.sub('fleur', 'flour', ing.lower())
        ing=re.sub('portabello', 'portobello', ing.lower())
        ing=re.sub('sausag', 'sausage', ing.lower())
        ing=re.sub('stout', 'fish', ing.lower())
        ing=re.sub('tilapia', 'fish', ing.lower())
        ing=re.sub('tawny port', 'tawny_port', ing.lower())
        ing=re.sub('trout', 'fish', ing.lower())
        ing=re.sub('eggs,1', 'egg', ing.lower())
        ing=re.sub('haddock', 'fish', ing.lower())
        ing=re.sub('hash browns', 'hash_brown', ing.lower())
        ing=re.sub('hash brown', 'hash_brown', ing.lower())
        ing=re.sub('mexicana', 'mexican', ing.lower())
        ing=re.sub('mexicorn', 'mexican', ing.lower())
        ing=re.sub('moong dal', 'moong_dal', ing.lower())
        ing=re.sub(r'\rose\b', 'rose_water', ing.lower())
        ing=re.sub('sausagee', 'sausage', ing.lower())
        ing=re.sub('sausagees', 'sausage', ing.lower())
        ing=re.sub('bawang goreng', 'bawang_goreng', ing.lower())
        ing=re.sub('buttermargarine', 'butter', ing.lower())
        ing=re.sub('margarine', 'butter', ing.lower())
        ing=re.sub('fishfish', 'fish', ing.lower())
        ing=re.sub('1', '', ing.lower())
        ing=re.sub('pig', 'pork', ing.lower())
        ing=re.sub('cardamom', 'cardamon', ing.lower())
        ing=re.sub('chiligarlic', 'chili', ing.lower())
        ing=re.sub('cornflake', 'corn', ing.lower())
        ing=re.sub('grouper', 'fish', ing.lower())
        ing=re.sub('soya bean', 'soybean', ing.lower())
        ing=re.sub('soya beans', 'soybean', ing.lower())
        ing=re.sub('softwheat', 'wheat', ing.lower())
        ing=re.sub('new york', '', ing.lower())
        ing=re.sub('barbecued', 'barbecue', ing.lower())
        ing=re.sub('bouquet garni', 'bouquet_garni', ing.lower())
        ing=re.sub('brie cheese', 'brie', ing.lower())
        ing=re.sub('pomegranate_seeds_seeds', 'pomegranate_seeds', ing.lower())
        ing=re.sub('channa_dal', 'chana_dal', ing.lower())
        ing=re.sub('chili_', 'chili', ing.lower())
        ing=re.sub('greenmulato', 'mulato', ing.lower())
        ing=re.sub('choy sum', 'choy_sum', ing.lower())



        

        



        

   
        ll = ing.lower().split()
        s = ''
        for word in ll:
            s = s + word + '#'
        s0.append(s[:-1])
        count += 1
        
    return ','.join(s0)  

###############################################

# custom-made stopwords
def stop_words(x=True):

    my_words = ['allpurpose', 'baby', 'black', 'boneless', 'breast', 'brown', 'chopped', 'coarse', 'cooked', \
    'cooking', 'crushed', 'dark', 'diced', 'dried', 'dry', 'extravirgin', 'fillet', 'flat', 'free', 'fresh', \
    'freshly', 'frozen', 'granulated', 'grated', 'green', 'ground', 'half', 'heavy', 'hot', 'kernel', 'kosher', \
    'large', 'leaf', 'light', 'low', 'lowfat', 'medium', 'minced', 'mix', 'peeled', 'plain', 'purple', 'red', \
    'reduced', 'roasted', 'sea', 'shredded', 'skinless', 'sliced', 'smoked', 'sodium', 'sour', 'spray', 'stick', \
    'sweet', 'toasted', 'unsalted', 'wedge', 'white', 'yellow', 'active', 'boiling', 'chip', 'cold', 'condensed', \
    'confectioner', 'cracked', 'crumbles', 'fine', 'finely', 'firm', 'flake', 'golden', 'greek', 'ice', 'lean', 'le',\
    'meal', 'monterey', 'nonfat', 'peel', 'pitted', 'powdered' ,'roast', 'shoulder', 'unsweetened', 'warm', \
    'basmati', 'chop', 'grain', 'longgrain', 'partskim', 'powder', 'shortening', 'style', 'sweetened', 'unsweetened', \
    'wrapper', 'extra', 'floret', 'long', 'roll', 'root', 'sharp', 'shell', 'slice', 'water', 'arborio', 'base', \
    'blackeyed', 'blend', 'bulb', 'button', 'canned', 'cube', 'drain', 'english', 'evaporated', 'flank', 'food', \
    'goat', 'gold', 'instant', 'juice', 'water', 'leg', 'liqueur', 'loin', 'mixed', 'packed', 'pure', 'purpose', \
    'refried', 'rind', 'pod', 'rom', 'romaine', 'russet', 'salted', 'seasoned', 'self', 'semisweet', 'snow', 'soda',\
    'soup', 'star', 'stewed', 'sundried', 'swiss', 'tea', 'thread', 'unbleached', 'whipping', 'baking', 'bittersweet',\
    'bone', 'chuck', 'country', 'dough', 'firmly', 'heart', 'kidney', 'melted', 'old', 'puff', \
    'reducedfat', 'round', 'sheet', 'shoot', 'slivered', 'small', 'salt', 'sugar', 'whipped', 'dressing',\
    'fatfree', 'fraiche', 'fruit', 'iceberg', 'jasmine', 'lower', 'maple', 'oil', 'prepared', 'refrigerated', \
    'soften', 'wing', 'belly', 'butt', 'chunky', 'concentrate', 'crumb', 'crust', 'soft', 'creamy', 'creme', 'piece',\
    'casing', 'liquid', 'seed', 'short', 'cap', 'colby', 'jack', 'coloring', 'crema', 'cremini', 'cut', 'dripping',\
    'elbow', 'flavored', 'granny', 'granule', 'hardboiled', 'leav', 'lump', 'mild', 'new', 'preserve', 'raw', \
    'ripe', 'seedless', 'shank', 'skim', 'skimmed', 'smith', 'steamed', 'stem', 'substitute', 'table', 'unflavored', \
    'vidalia', 'wild', 'bag', 'baked', 'blanched', 'blue', 'brewed', 'candied', 'crumbled', 'ear', 'eye', 'grating', \
    'knorr', 'lima', 'link', 'pickled', 'preserved', 'superfine', 'whip', 'beaten', 'best', 'boston', 'bottled', \
    'bought', 'california', 'cane', 'crescent', 'crusty', 'dipping', 'double', 'drained', 'dri', 'file', 'filet', \
    'flaked', 'fry', 'glutinous', 'gram', 'great', 'northern', 'rock', 'rubbed', 'savoy', 'scotch', 'shelled', \
    'shortgrain', 'silken', 'skin', 'skirt', 'softened', 'spicy', 'spear', 'split', 'sprinkle', 'store', 'stuffed', \
    'thickcut', 'topping', 'uncook', 'beer', 'center', 'chunk', 'club', 'cooky', 'deli', 'delicious', 'deveined', \
    'dusting', 'essence', 'finger', 'flower', 'fried', 'gluten', 'ha', 'haricot', 'homemade', 'hothouse', 'hungarian',\
    'irish', 'littleneck', 'mini', 'navel', 'nonstick', 'paso', 'pickling', 'processed', 'quickcooking', 'ra', 'ragu',\
    'real', 'regular', 'rising', 'selfrising', 'simple', 'stir', 'tamari', 'ton', 'american', 'bertolli', 'bonnet', \
    'breakfast', 'brinecured', 'crystallized', 'fermented', 'filling', 'glass', 'heirloom', 'jumbo', 'lan', \
    'malt', 'neutral', 'nosaltadded', 'organic', 'original', 'ovenready', 'pink', 'rabe', 'range', 'roasting', \
    'stuffing', 'sweeten', 'sweetener', 'tip', 'turbinado', 'wood', 'bitter', 'clarified', 'cocktail', 'colouring', \
    'cook', 'grate', 'lowsodium', 'marin', 'oz', 'paper', 'quarter', 'ripened', 'rolled', 'rotel', 'sec', 'smoke', \
    'sparerib', 'sticky', 'strip', 'summer', 'triple', 'vegan', 'blossom', 'flavoring', 'flavor', 'glutenfree', \
    'grand', 'loosely', 'prepar', 'waxy', 'wide', 'belgian', 'navy', 'philadelphia', 'stewing', 'tiger', 'quick', \
    'shucked', 'cornish', 'straw', 'nutritional', 'thawed', 'bar', 'beefsteak', 'believe', 'bibb', 'blood', \
    'boil', 'bosc', 'brine', 'bulk', 'campbell', 'canadian', 'crush', 'cubed', 'cured', 'curly', 'doubleacting',\
    'dutchprocessed', 'fingerling', 'grease', 'hard', 'johnsonville', 'juniper', 'meyer', 'muscovado', 'natural', \
    'non', 'oilcured', 'persian', 'piecrusts', 'pound', 'rub', 'salata', 'season', 'sel', 'spray,1', 'squeezed', \
    'string', 'tawny', 'tender', 'zesty', '1', 'bit', 'boiled', 'bran', 'browning', 'chickenflavored', 'clear', \
    'color', 'crock', 'fryer', 'gum', 'imitation', 'mission', 'pulp', 'rins', 'uncooked', 'unbaked', 'world', \
    'yardlong', 'aged', 'amaretti', 'ball', 'bartlett', 'bicarbonate', 'buffalo', 'clove', 'devein', 'dinner', \
    'distilled', 'field', 'fully', 'honeydew', 'lite', 'madras', 'mediumgrain', 'nectar', 'pace', 'silver', 'size', \
    'solid', 'sugar,1', 'swanson', 'pepper', 'onion', 'garlic', 'sauce', 'wine', 'liquor', 'liquer', 'beer', \
    'added', 'bread', 'breadcrumb', 'bun', 'cake', 'coffee', 'equal', 'espresso', 'farmer', 'flora', 'germ', \
    'guinness', 'hand', 'head', 'ice_cream', 'jello', 'king', 'lemonade', 'limeade', 'medjool', 'muffin', \
    'onion', 'poultry', 'rack', 'rapid', 'softboiled', 'sourdough', 'spice', 'stone', 'vegetarian', 'virgin', \
    '2', 'ale', 'candy', 'carbonated', 'dip', 'game', 'palm', 'paste', 'ring', 'seltzer', 'spare', 'stoneground', \
    'strong', 'wrap', 'asian', 'italian', 'mexican', 'reducedsodium', 'runny', 'single', 'spread', 'applesauce', \
    'applewood', 'bisquick', 'bonein', 'bouillon', 'canola', 'cherry', 'chinese', 'chocolate', 'cider', 'classico', \
    'cocoa', 'confit', 'converted', 'cranberry', 'curd', 'custard', 'dungeness', 'el', 'extract', 'farm', 'fat', \
    'flour', 'french', 'gala', 'garden', 'genoa', 'graham', 'grapeseed', 'hock', 'husk', 'idaho', 'kidnei', \
    'kirby', 'lemonlime', 'lipton', 'mandarin', 'napa', 'neck', 'nicoise', 'pack', 'pancake', 'panko', 'pearl', \
    'phyllo', 'plum', 'porkeon', 'puree', 'rib', 'rise', 'rump', 'safflower', 'serrano', 'shaving', 'shellon', 'shiro', \
    'shuck', 'splenda', 'spring', 'starch', 'tail', 'tenderloin', 'toast', 'tongue', 'turkish', 'verde', 'vine', 'yukon', \
    'bengal', 'biryani', 'blackberry', 'blanco', 'blueberry', 'caesar', 'calimyrna', 'carnaroli', 'cocacola', 'cool', \
    'fleshed', 'foot', 'kikkoman', 'lacinato', 'oldfashioned', 'parboiled', 'rendered', 's', 'sanding', 'slab', 'sparkling', \
    'sprite', 'steelcut', 'sub', 'valley', 'varnish', 'winter', 'crystal', 'cuban', 'cuisine', 'demerara', 'hidden', 'min', \
    'oscar', 'broilerfryer', 'prebaked']

    return(my_words)

    ###############################################


