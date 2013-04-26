#!/bin/bash
## Check if the columns have proper data in them

buildings=( Hatchery SpawningPool BanelingNest EvolutionChamber Extractor GreaterSpire Hive HydraliskDen MorphOverlord InfestationPit Lair NydusWorm RoachWarren SpineCrawler SporeCrawler Spire UltraliskCavern Armory Barracks Bunker CommandCenter EngineeringBay Factory FusionCore GhostAcademy MissileTurret OrbitalCommand PlanetaryFortress Reactor Refinery SensorTower Starport SupplyDepot TechLabFactory TechLabStarport ReactorFactory ReactorStarport ReactorBarracks TechLabBarracks Pylon Assimilator CyberneticsCore DarkShrine FleetBeacon Forge Gateway Nexus PhotonCannon RoboticsBay RoboticsFacility Stargate TemplarArchives TwilightCouncil WarpGate )

for building in "${buildings[@]}"
do 
echo $building
done


while read line; do
    name=`grep $line $1 | cut -d, -f10`
    name2=`grep $line $1 | cut -d, -f20`
    matched=0
    for i in "${buildings[@]}"; do
        
	if [ "$name" == "$i" ];
	then

	   # if [ "$name2" == "$i" ];
	   # then	
	    matched=1
	    echo "We have a match ladies and gents." $name $i
	    echo $line >> newData.txt
#	    fi
	fi
    done
    if [ $matched -eq 0 ]
    then
	echo $name $line "**************************************************"
	sleep 1
    fi
done < $1


#    for i in "${buildings[@]}"
#    do
#	echo $i
#	if [ "$i" == "Dully" ] ; then
#	    echo "found"
#	fi
#   done

#done < $1


#grep  $1 | cut -d, -f10