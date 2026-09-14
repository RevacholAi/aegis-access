# server.py
import logging
from mcp.server.mcpserver import MCPServer

logging.basicConfig(level=logging.INFO) #Configurer les logs sur stderr pour eviter de passer par le canal stdio
logger = logging.getLogger(__name__)#Protocole mcp interdit d'utiliser print() pour déboguer dans un serveur basé sur STDIO

#initialize the FastMCP server
mcp = MCPServer("aegis-access-lab")
taches=["Finir Crime et Chatiment","Faire les courses","Sport"] 

@mcp.resource("liste://taches")
def lireListe() -> str:
###les guillemets present en dessous sont tres importanes car elles vont a l'ia l'utilisation des fonctions 
    """Permet à l'IA de lire la liste actuelle des taches """

    if not taches:
        return "la liste est vide "
    return " , ".join(taches)


@mcp.tool()
def ajouter_tache(nouvelle_tache:str) -> str:

    """ajouter une nouvelle tache a la liste de l'utilisateur"""

    taches.append(nouvelle_tache)
    return f"Succés : '{nouvelle_tache}' a été ajouté a la liste !"

if __name__== "__main__":
    mcp.run()#démarre le serveur