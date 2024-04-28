from flask import Flask, request, jsonify
app = Flask("app")

@app.route("/")
def main():
    getreqeust = request.args.get("name")
    if getreqeust=="null":
       getreqeust=""
    desc=""
    #Uncommon
    if getreqeust.lower()=="basic":
      desc="Basic doesn't mean bad. Rough around the edges, but can be just as effective as other styles with its balanced stats. Ultimate: Full Force Uppercut"
    elif getreqeust.lower()=="smash":
       desc="Tough, gritty, and crude. Signature attack is the Smash Punch - a half-hook-half-uppercut that deals high damage (bonus to blocking victims) but is hard to land and follow up with. Ultimate: Smash Punch Finisher"
    elif getreqeust.lower()=="long guard":
       desc="With the lead hand out that far, your jab is probably going to land first. Faster startup and punches in exchange for slightly weaker light punches and dash. Ultimate: 1-1-2"
    elif getreqeust.lower()=="turtle":
       desc="Operation Turtle is a defensive strategy where a user shells up and waits for an opportunity to attack. Although your dashes are weak, you have a very strong guard that recovers quickly. Ultimate: One Centimeters Punch"
    
    #Rare
    elif getreqeust.lower()=="corkscrew":
       desc="All punches are light compared to the burden of being a champion. You recover your health faster and have a high-damaging heavy attack: the Corkscrew punch, but slower startup. Ultimate: Heartbreak Shot"
    elif getreqeust.lower()=="counter":
       desc="Precision beats power, timing beats speed. Your punches do less damage, but you get a huge damage bonus on counter and have a good dash. Ultimate: Jolt Blow"
    elif getreqeust.lower()=="trickster":
       desc="Although you look goofy, you're hard to read. Weird punches and insanely fast dash cancels make you hard to hit. Great mobility, weaker block. Ultimate: Look-Away Frog Punch"
    elif getreqeust.lower()=="kimura":
       desc="Your style was always basic, and you don't have the same level of talent as others. But you’re far more determined. Your bodyshots can SLOW DOWN an opponent, letting you land your finishing move. Ultimate: Dragonfish Blow"
    elif getreqeust.lower()=="charge":
       desc="You can run, but you can't hide. A hyper-aggressive, textbook in-fighter who doesn't know the meaning of stepping backwards. Unique Ability: Stampede - charges into your opponent, unleashing powerful body shots that sap their stamina Ultimate: Raging Bull"
    
    #Mythic
    elif getreqeust.lower()=="ippo":
       desc="Using a variation of the Peek-a-boo style, Ippo is an in-fighter with a barrage of hooks to the head and body, along with rib-cracking and jaw-breaking uppercuts. Good damage, good dash, slower startup. Ultimate: Dempsey Roll"
    elif getreqeust.lower()=="wolf":
       desc="A textbook style with no major downsides- and a unique ability. You can double up on your M2 and execute a White Fang, dealing extra damage and block break. Ultimate: True White Fang"
    elif getreqeust.lower()=="bullet":
       desc="A combination of insane talent, arrogance, and absolutely killer instinct. Your heavy Thunderbolt attacks deal high counter damage, but your base damage and dash are weak. Special Ability: your bullet jabs come out instantly if you fire after an opponent dashes. Ultimate: Cheating Combo"
    elif getreqeust.lower()=="shotgun":
       desc="With a unique ability that lets you throw rapid jabs as if your hand was a shotgun, and well rounded stats you are a true prodigy. However the price to pay for your abilities are a glass jaw that is very weak to counter damage. Ultimate: Target Practice"
    elif getreqeust.lower()=="hands Low":
       desc="Fast, sharp, technical - but having your hands down is risky. Great dash, start speed, and slight counter bonus at the cost of taking more counter damage. Ultimate: Blinding Rush"
    
    #Legendary
    elif getreqeust.lower()=="hitman":
       desc="Punishes others with devastating flicker jabs, and chopping rights. Fast startup with good range, great damage, but weak dash. Ultimate: Nightmare Barrage"
    elif getreqeust.lower()=="slugger":
       desc="A genius in the ring with overwhelming power - you throw every shot with 110%. Weak dash and block, but amazing punch damage and a unique ability: charging up your heavy attacks. Ultimate: Rage"
    elif getreqeust.lower()=="huwk":
       desc="In your madness, you only rely on your instincts and lose sight of what's in front of you. Ability: Swayback. Ultimate: Pure Violence"
    elif getreqeust.lower()=="ghost":
       desc="He who rules with his left rules the world.' Like a ghost your punches are hard to see coming. Special Ability: Ghost Jab - you can fire of a near-instant, unreadable punch to start combos. However, if you miss or it gets blocked, you will get stunned. Ultimate: Goodbye"
    elif getreqeust.lower()=="iron fist":
       desc="Nothing is a greater short-cut than hard work. Your hands were forged from hard training and deal MASSIVE damage and inflict slowing, but HURT you when you land them. On top of that, you take less damage when being countered while throwing your heavy punches. Ultimate: No Ribs Survived"
    elif getreqeust.lower()=="freedom":
       desc="You are not bound to a single style, since inside the ring, you are absolutely free. Unique ability: you can swap between 3 different modes (Whirlwind, Flicker, Smash) that each have advantages and disadvantages. However, you are very fragile. Ultimate: Last Sun"
    elif getreqeust.lower()=="chronos":
       desc="While your punches may lack sting, your true strength manifests when you focus your concentration to its upper limits. Ability: Focus - emoting, countering, and perfect dodging all build up a meter that allows you to access your full potential. Ultimate: Bullet Time"
       

    return jsonify({     
       "description": desc,
       "name": getreqeust
    })

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')
