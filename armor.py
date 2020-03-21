dmg_taken = 30.0
prot        = 0
speed_per   = 1.0
armor       = 0.0
armor_per   = 1.0
toughness   = 0.0
evasion     = 0
health_per  = 1.0
atk_spd_per = 1.0
atk_dmg_per = 1.0
arw_spd_per = 1.0
bow_atk_dmg_per = 1.0
helm_name   = ""
chest_name  = ""
pants_name  = ""
boots_name  = ""
hand_name   = ""
health      = 20.0
speed       = 0.15
atk_dmg     = 10.0
bow_atk_dmg = 10.0
total_armor = 0.0
total_speed_per = 0.0
total_health = 0.0
total_atk = 0.0
total_bow_atk = 0.0
per_dmg_taken = 1.0
second_wind = 0

def helmet(i):
	global prot, speed_per, armor, armor_per, toughness, evasion, health_per, atk_spd_per, atk_dmg_per, arw_spd_per, bow_atk_dmg_per, helm_name, chest_name, pants_name, boots_name, hand_name, health, speed, atk_dmg, bow_atk_dmg
	if i==0:
		helm_name = "Cursestone Helm"
		prot += 1
		armor += 1.5
		toughness += 0.5
	if i==1:
		helm_name = "Embalmer\'s Wrap"
		armor += 2.0
		toughness += 1.0
	if i==2:
		helm_name = "Excavator\'s Hardlamp"
		prot += 2
		speed_per += -0.05
		armor += 2.5
		toughness += 1.5
	if i==3:
		helm_name = "Frost Giant\'s Crown"
		speed_per += -0.05
		armor += 6
		toughness += 3
	if i==4:
		helm_name = "Horseman\'s Head"
		speed_per += 0.15
		prot += 5
	if i==5:
		helm_name = "Phantom Pirate\'s Cap"
		prot += 1
		evasion += 2
		armor += 0.5
	if i==6:
		helm_name = "Reaper\'s Hood"
		prot += 2
		armor += 2.5
		toughness += 1.5
	if i==7:
		helm_name = "Seadiver\'s Shell"
		armor += 3
	if i==8:
		helm_name = "Shimmerscale Remnant"
		evasion += 2
		armor += 2
	if i==9:
		helm_name = "Silkshine Hood"
		evasion += 2
		speed_per += 0.05
		armor += 1
	if i==10:
		helm_name = "Tithe of the Tides"
		prot += 3
		health += 2
		armor += 1.5
		toughness += 0.5
	if i==11:
		helm_name = "Xeno\'s Pirate Hat"
		prot += 4
		armor += 1
	if i==12:
		helm_name = "Crown of Flames"
		prot += 2
		bow_atk_dmg_per += 0.15
		armor += 2
		toughness += 1
	if i==13:
		helm_name = "Invigorating Paddy Hat"
		evasion += 2
		health += 6
		armor += 1
	if i==14:
		helm_name = "Sacrifice\'s Scalp"
		prot += 2
		health += 2
		armor += 1
	if i==15:
		helm_name = "Lunar Great Helm"
		prot += 2
		atk_dmg += 2
		armor += 2
	if i==16:
		helm_name = "Rusty Diving Helmet"
		prot += 1
		speed_per += -0.08
		armor += 4
		toughness += 4
	if i==17:
		helm_name = "Rageroot Crown"
		evasion += 2
		atk_dmg_per += 0.20
		armor += 1.5
		toughness += 0.5
	if i==18:
		helm_name = "Adamantium Skin"
		armor += 3
		toughness += 3
	if i==19:
		helm_name = "Veil of the Blizzard"
		prot += 3
		armor += 2
		toughness += 1

def chestplate(i):
	global prot, speed_per, armor, armor_per, toughness, evasion, health_per, atk_spd_per, atk_dmg_per, arw_spd_per, bow_atk_dmg_per, helm_name, chest_name, pants_name, boots_name, hand_name, health, speed, atk_dmg, bow_atk_dmg
	if i==0:
		chest_name = "Bounty Hunter\'s Gambeson"
		prot += 2
		evasion += 2
		armor += 6
	if i==1:
		chest_name = "Cursestone Chestplate"
		prot += 2
		armor += 4
		toughness += 0.5
	if i==2:
		chest_name = "Embalmer\'s Chains"
		armor += 5
		toughness += 1
	if i==3:
		chest_name = "Harmonic Tunic"
		prot += 2
		speed_per += 0.05
		atk_spd_per += 0.05
		atk_dmg_per += 0.05
		armor += 3
	if i==4:
		chest_name = "Myriad\'s Embrace"
		prot += 4
		speed_per += 0.10
		armor += 4
		toughness += 0.5
	if i==5:
		chest_name = "Phasing Chestplate"
		evasion += 4
		speed += 0.02
		speed_per += -0.10
		armor += 4
		toughness += 3
	if i==6:
		chest_name = "Reaper\'s Cloak"
		prot += 3
		armor += 4.5
		toughness += 2
	if i==7:
		chest_name = "Silkshine Cloak"
		evasion += 3
		speed_per += 0.10
		armor += 3
	if i==8:
		chest_name = "Archangel\'s Mail"
		evasion += 2
		health += 4
		armor += 5
		toughness += 1
	if i==9:
		chest_name = "Leafveil Shroud"
		health += 2
		speed_per += 0.12
		bow_atk_dmg += 2
		armor += 5
		toughness += 1
	if i==10:
		chest_name = "Wings of Alutana"
		prot += 4
		speed_per += -0.10
		armor += 5
		toughness += 1
	if i==11:
		chest_name = "Flameborn Runeplate"
		prot += 3
		evasion += 1
		atk_spd_per += 0.08
		atk_dmg_per += 0.15
		armor += 4
		toughness += 0.5
	if i==12:
		chest_name = "Heart of the Sea"
		prot += 5
		armor += 3
	if i==13:
		chest_name = "Phoenix Shroud"
		prot += 3
		health += 6
		armor += 2
	if i==14:
		chest_name = "Varcosa\'s Doublet"
		evasion += 3
		speed_per += 0.15
		atk_spd_per += 0.15
		armor += 2
	if i==15:
		chest_name = "Adamantium Skin"
		armor += 7
		toughness += 3
	if i==16:
		chest_name = "Cape of the Blizzard"
		prot += 4
		armor += 5
		toughness += 1

def pants(i):
	global prot, speed_per, armor, armor_per, toughness, evasion, health_per, atk_spd_per, atk_dmg_per, arw_spd_per, bow_atk_dmg_per, helm_name, chest_name, pants_name, boots_name, hand_name, health, speed, atk_dmg, bow_atk_dmg
	if i==0:
		pants_name = "Cursestone Greaves"
		prot += 2
		armor += 3
		toughness += 0.5
	if i==1:
		pants_name = "Embalmer\'s Leggings"
		armor += 4
		toughness += 1
	if i==2:
		pants_name = "Ethereal Greaves"
		evasion += 3
		speed_per += 0.12
		arw_spd_per += 0.20
		armor += 4
		toughness += 1
	if i==3:
		pants_name = "Frost Knight\'s Greaves"
		speed_per += -0.10
		atk_dmg += 2
		armor += 6
		toughness += 3
	if i==4:
		pants_name = "Harmonic Leggings"
		prot += 2
		speed_per += 0.05
		health_per += 0.05
		atk_spd_per += 0.05
		atk_dmg_per += 0.05
		armor += 2
	if i==5:
		pants_name = "Madman\'s Leggings"
		prot += 4
		speed += 0.20
		health += -4
		armor += 3
		toughness += 0.5
	if i==6:
		pants_name = "Persistent Chains"
		speed_per += 0.10
		atk_dmg += 1
		armor += 4
		toughness += 1.5
	if i==7:
		pants_name = "Phantom Pirate\'s Trousers"
		prot += 1
		evasion += 3
		armor += 1
	if i==8:
		pants_name = "Silkshine Trousers"
		evasion += 3
		speed_per += 0.10
		armor += 2
	if i==9:
		pants_name = "Sunblessed Leggings"
		prot += 3
		health += 3
		armor += 3
		toughness += 0.5
	if i==10:
		pants_name = "Laborious Chains"
		prot += 3
		#atk_spd += 0.1
		armor += 4
		toughness += 1
	if i==11:
		pants_name = "Aqueduct Greaves"
		evasion += 2
		health_per += 0.20
		armor += 2
	if i==12:
		pants_name = "Adamantium Skin"
		armor += 6
		toughness += 3
	if i==13:
		pants_name = "Leggings of the Blizzard"
		prot += 4
		armor += 4
		toughness += 1

def boots(i):
	global prot, speed_per, armor, armor_per, toughness, evasion, health_per, atk_spd_per, atk_dmg_per, arw_spd_per, bow_atk_dmg_per, helm_name, chest_name, pants_name, boots_name, hand_name, health, speed, atk_dmg, bow_atk_dmg, second_wind
	if i==0:
		boots_name = "Boots of Alutana"
		prot += 3
		armor += 2
		toughness += 1
	if i==1:
		boots_name = "Daredevil\'s Wake"
		prot += 2
		speed_per += 0.15
		health += 6
	if i==2:
		boots_name = "Dune Raider\'s Treads"
		evasion += 2
		speed_per += 0.10
		atk_dmg_per += 0.25
		bow_atk_dmg_per += 0.25
		armor += 0.5
	if i==3:
		boots_name = "Salazar\'s Spats"
		prot += 2
		speed_per += 0.12
		atk_spd_per += 0.10
		armor += 1.5
		toughness += 0.5
	if i==4:
		boots_name = "Scarlet Ward"
		evasion += 2
		armor += 2
	if i==5:
		boots_name = "Varcosa\'s Cavaliers"
		evasion += 3
		armor += 1
		second_wind += 1
	if i==6:
		boots_name = "Warm Crystal Boots"
		health += 3
		armor += 3
	if i==7:
		boots_name = "Steel Sabatons"
		prot += 2
		armor += 2.5
		toughness += 1.5
	if i==8:
		boots_name = "Locust\'s Sandals"
		evasion += 1
		health += 4
		bow_atk_dmg += 2
	if i==9:
		boots_name = "Ifrit\'s Sandals"
		prot += 3
		speed_per += 0.10
		armor += 1.5
		toughness += 0.5
	if i==10:
		boots_name = "Chains of the Damned"
		prot += 4
		speed_per += -0.10
		armor += 1
	if i==11:
		boots_name = "Adamantium Skin"
		armor += 3
		toughness += 3
	if i==12:
		boots_name = "Veil of the Blizzard"
		prot += 3
		armor += 2
		toughness += 1
	if i==13:
		boots_name = "Stoneskin Boots"
		prot += 1
		armor += 1
		toughness += 5

def hand(i):
	global prot, speed_per, armor, armor_per, toughness, evasion, health_per, atk_spd_per, atk_dmg_per, arw_spd_per, bow_atk_dmg_per, helm_name, chest_name, pants_name, boots_name, hand_name, health, speed, atk_dmg, bow_atk_dmg
	if i==0:
		hand_name = "Ash Codex"
		health += 2
	if i==1:
		hand_name = "Celsian Sarissa"
		evasion += 2
		armor += 2
	if i==2:
		hand_name = "Embalmer\'s Trophy"
		armor_per += 0.25
	if i==3:
		hand_name = "Merchant\'s Curio"
		evasion += 4
		speed_per += 0.18
		atk_dmg_per += -0.25
	if i==4:
		hand_name = "Metamorphosis"
		armor += 3
		speed_per += 0.16
	if i==5:
		hand_name = "Royal Shield"
		atk_dmg += 1
	if i==6:
		hand_name = "The Eternal Mist"
		evasion += 3
		armor += 1
	if i==7:
		hand_name = "Tiffy\'s Shield"
		evasion += 2
		speed_per += 0.15
	if i==8:
		hand_name = "Tube of Toothpaste"
		health_per += 0.30
		armor += 1
	if i==9:
		hand_name = "Necronomicon"
		evasion += 2
		speed_per += 0.20
		atk_dmg_per += 0.20
	if i==10:
		hand_name = "Sandblaster"
		atk_dmg_per += 0.25
		atk_dmg += 1
		armor += 2
	if i==11:
		hand_name = "Icicle\'s Bulwark"
		health += 2
		armor += 2
		toughness += 2
	if i==12:
		hand_name = "Dissonant Dagger"
		health_per += 0.20
		health += -2
		speed_per += 0.10
		atk_spd_per += 0.10
		atk_dmg += -1
		atk_dmg_per += 0.20
	if i==13:
		hand_name = "Warding Lily"
		health += 2
		#atk_spd += 0.15
		atk_dmg_per += 0.05
	if i==14:
		hand_name = "Sahra Ib"
		health_per += 0.15
	if i==15:
		hand_name = "Necromancer\'s Sigil"
		health += 10
	if i==16:
		hand_name = "Moonbeam Dagger"
		health += 2
		atk_dmg_per += 0.35
	if i==17:
		hand_name = "Tear of the Moon"
		speed_per += 0.05
		health += 2
		armor += 3
	if i==18:
		hand_name = "Bloodletter\'s Dagger"
		speed_per += -0.05
		health += 4
		atk_dmg_per += 0.15
	if i==19:
		hand_name = "Abyssal Buckler"
		speed_per += 0.15
		atk_dmg += 2
		armor += 2
	if i==20:
		hand_name = "Steel Maelstrom"
		evasion += 3
		atk_spd_per += 0.10
		atk_dmg_per += 0.20
	if i==21:
		hand_name = "Dragonbone Dagger"
		health += 2
		speed += 0.02
		atk_dmg_per += 0.10
		atk_dmg += 2
	if i==22:
		hand_name = "Steel Bracer"
		armor += 3
		toughness +=3


def totals():
	global dmg_taken, prot, speed_per, armor, armor_per, toughness, evasion, health_per, atk_spd_per, atk_dmg_per, arw_spd_per, bow_atk_dmg_per, helm_name, chest_name, pants_name, boots_name, hand_name, health, speed, atk_dmg, bow_atk_dmg,second_wind
	total_armor = armor*armor_per
	total_speed_per = speed*speed_per/0.15
	total_health = health*health_per
	total_atk = atk_dmg*atk_dmg_per
	total_bow_atk = bow_atk_dmg*bow_atk_dmg_per

	if evasion >= 10:
		dmg_taken *= 0.60
	elif evasion >= 20:
		dmg_taken *= 0.20

	abs_armor_reduct = 0.04*min(20.0,max(total_armor/5.0,total_armor-(dmg_taken/(2.0 + (toughness/4.0)))))
	abs_prot_reduct  = 0.0
	if prot < 20:
		abs_prot_reduct = prot/25.0
	elif prot >= 20:
		abs_prot_reduct = 0.80

	abs_dmg_taken  = dmg_taken*(1-abs_prot_reduct)*(1-abs_armor_reduct)-((second_wind)**0.5)
	per_dmg_taken  = abs_dmg_taken/total_health
	return(total_armor,total_speed_per,total_health,total_atk,total_bow_atk,abs_dmg_taken,per_dmg_taken)

least_dmg_taken  = 30.0
least_per_dmg_taken = 1.0
best_prot        = 0
best_armor       = 0.0
best_toughness   = 0.0
best_evasion     = 0
best_speed_per   = 0.0
best_health      = 0.0
best_atk         = 0.0
best_atk_spd_per = 0.0
best_bow_atk     = 0.0
best_arw_spd_per = 0.0
best_helm_name   = ""
best_chest_name  = ""
best_pants_name  = ""
best_boots_name  = ""
best_hand_name   = ""

indices_of_best  = [0,0,0,0,0]

for i in range(20):
	for j in range(17):
		for k in range(14):
			for m in range(14):
				for n in range(23):
					dmg_taken   = 30.0
					prot        = 0
					speed_per   = 1.0
					armor       = 0.0
					armor_per   = 1.0
					toughness   = 0.0
					evasion     = 0
					health_per  = 1.0
					atk_spd_per = 1.0
					atk_dmg_per = 1.0
					arw_spd_per = 1.0
					bow_atk_dmg_per = 1.0
					second_wind = 0
					helm_name   = ""
					chest_name  = ""
					pants_name  = ""
					boots_name  = ""
					hand_name   = ""
					health      = 20.0
					speed       = 0.15
					atk_dmg     = 10.0
					bow_atk_dmg = 10.0
					total_armor = 0.0
					total_speed_per = 0.0
					total_health = 0.0
					total_atk = 0.0
					total_bow_atk = 0.0
					abs_dmg_taken = 0.0
					helmet(i)
					chestplate(j)
					pants(k)
					boots(m)
					hand(n)
					total_armor,total_speed_per,total_health,total_atk,total_bow_atk,abs_dmg_taken,per_dmg_taken = totals()
					if abs_dmg_taken < least_dmg_taken:
						least_dmg_taken = abs_dmg_taken
						least_per_dmg_taken = per_dmg_taken
						indices_of_best = [i,j,k,m,n]
						best_prot        = prot
						best_armor       = total_armor
						best_toughness   = toughness
						best_evasion     = evasion
						best_speed_per   = total_speed_per
						best_health      = total_health
						best_atk         = total_atk
						best_atk_spd_per = atk_spd_per
						best_bow_atk     = total_bow_atk
						best_arw_spd_per = arw_spd_per
						best_helm_name   = helm_name
						best_chest_name  = chest_name
						best_pants_name  = pants_name
						best_boots_name  = boots_name
						best_hand_name   = hand_name

print("30 initial damage")
print(least_dmg_taken, "damage taken")
print(least_per_dmg_taken*100, "percent total health taken")
print("**Build**")
print(best_helm_name)
print(best_chest_name)
print(best_pants_name)
print(best_boots_name)
print(best_hand_name)
print(best_prot, "Protection")
print(best_armor, "Armor")
print(best_toughness, "Toughness")
print(best_evasion, "Evasion")
print("+", (best_speed_per - 1)*100, "Speed")
print(best_health, "Total Max Health")
print("+", best_atk - 10, "Attack Damage")
print("+", (best_atk_spd_per - 1)*100, "Attack Speed")
print("+", best_bow_atk - 10, "Bow Damage")
print("+", (best_arw_spd_per-1)*100, "Arrow Speed")













