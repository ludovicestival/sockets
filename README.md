## TP A

### Etape 1

A quel moment la socket côté serveur est-elle bloquante ?

Au moment de l'appel de la méthode recv.

Que se passe-t-il si le client se connecte avant que le serveur ne soit prêt ?

Le code du client va planter avec une exception ConnectionRefusedError.

Quelle est la différence entre bind et listent ?

bind permet d'associer une addresse avec un port. listen autorise les connections entrantes.

### Etape 2

Pourquoi faut-il une boucle dans le serveur ?

Sans boucle, le serveur s'arrêtera dès qu'il aura renvoyé le premier message reçu.

Que se passe-t-il si on oublie de tester msg == 'fin' ?

Le serveur ne s'arrêtera pas s'il reçoit ce message particulier.

Est-ce que le serveur peut envoyer plusieurs réponses d'affilée ?

Non, il faut d'abord qu'il recoive un message.

### Etape 3

Le serveur peut-il rester actif après une déconnexion client ?

Oui, il va juste attendre la prochaine connexion.

Que faut-il modifier pour accepter plusieurs clients à la suite ?

Peut-on imaginer accepter des clients en parallèle ?

### Etape 4

Comment s'assurer que les deux côtés ne parlent pas en même temps ?

Dès qu'on utilise la méthode recv, cela va bloquer le programme dans l'attente d'un message.

Peut-on rendre cet échange non bloquant ?

Oui en utilisant des threads.

Quelle est la meilleure façon de quitter proprement la communication ?

On peut utilisater la méthode close des sockets.

### Etape 5

Quels sont les risques d'utiliser eval ?

En utilisant eval, le serveur execute le code donné par l'utilisateur, ce qui est une très mauvaise idée. En effet, cela pose un problème de sécurité car l'utilisateur peut accéder à la machine et y faire ce qu'il veut grâce à des librairies Python comme os ou subprocess.

Comment renvoyer une erreur sans faire planter le serveur ?

On peut utiliser une structure try catch.

### Etape 6

Pourquoi structurer les messages avec /commande ?

Cela permet au serveur de proposer plusieurs services selon la commande utilisée. De plus, si toutes les commandes ont la même structure,
cela en facilite le traitement.

Comment distinguer facilement les types de messages côté serveur ?

On peut utiliser la partie du message qui spécifie la commande.
