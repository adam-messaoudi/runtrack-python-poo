class Commande:
    def __init__(self, numero_commande, liste_commande):
        # Initialise les attributs de la commande
        self._numero_commande = numero_commande
        self._liste_commande = liste_commande
        self._statut_commande = "En cours"  # Initialise le statut de la commande comme "En cours"

    def _calculer_total(self):
        # Méthode privée pour calculer le total de la commande
        return sum(self._liste_commande.values())

    def ajouter_plat(self, plat, prix):
        # Méthode pour ajouter un plat à la commande avec son prix
        self._liste_commande[plat] = prix

    def annuler_commande(self):
        # Méthode pour annuler une commande en mettant à jour le statut
        self._statut_commande = "Annulée"

    def _calculer_tva(self):
        # Méthode privée pour calculer la TVA sur le total de la commande
        total = self._calculer_total()
        return total * 0.20  # Supposons un taux de TVA de 20%

    def afficher_commande(self):
        # Méthode pour afficher les détails de la commande avec le total HT, la TVA et le total TTC
        total = self._calculer_total()
        tva = self._calculer_tva()
        infos_commande = (
            f"Numéro de commande: {self._numero_commande}\n"
            f"Statut de la commande: {self._statut_commande}\n"
            f"Plats commandés:\n"
        )
        for plat, prix in self._liste_commande.items():
            infos_commande += f"- {plat}: {prix}€\n"
        infos_commande += (
            f"----------------\n"
            f"Total HT: {total}€\n"
            f"TVA: {tva}€\n"
            f"Total TTC: {total + tva}€"
        )
        return infos_commande


def tester_commande():
    # Fonction pour tester la classe Commande
    plat_commande = {
        "Pizza": 10.00,
        "Salade": 5.00,
        "Boisson": 2.50
    }

    commande = Commande(1, plat_commande)
    print(commande.afficher_commande())  # Affichage des détails de la commande

    commande.ajouter_plat("Dessert", 4.00)  # Ajout d'un plat à la commande
    commande.annuler_commande()  # Annulation de la commande
    print(commande.afficher_commande())  # Affichage après annulation


if __name__ == "__main__":
    tester_commande()
