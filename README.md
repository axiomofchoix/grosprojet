J'ai fait le début, tu peux repasser sur mon code pour voir comment ca marche et si tu veux modifier mon implémentation des caisses et de l'herbe parce que j'ai fait des trucs pas tres beaux.

Essaye de faire un peu les mouvements, et de mettre en ordre les documents(je crois qu'il faut un fichier log par exemple).

la méthodologie est toujours la même:

-tu fais "git pull" pour choper la dernière version du git (tu corriges les eventuels conflits avec ta version)
-tu modifies ce que tu veux
-tu fais "git add ." pour ajouter toutes les modifications (tu peux faire fichier par fichier sinon)
-tu fais "git commit -m "ton message"" avec toujours un message sinon il va te casser les couilles
-tu fais git push pour le foutre sur le git principal avec ton mot de passe (s'il y a deja eu un push entre temps tu refais just un pull et tu regles les conflits)

si tu veux plus d'infos tu vas sur le tuto "branches" mais normalement c'est ça
