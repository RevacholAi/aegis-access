# server.py
import os 
import json
from datetime import datetime, timezone
import subprocess
import logging
from mcp.server.mcpserver import MCPServer

logging.basicConfig(level=logging.INFO) #Configurer les logs sur stderr pour eviter de passer par le canal stdio
logger = logging.getLogger(__name__)#Protocole mcp interdit d'utiliser print() pour déboguer dans un serveur basé sur STDIO

def log_app(nomtool, args ,com): #Indique a quelle heure et quelle outil a ete applique avec des arguments
    entre = {
        "timestamp":datetime.now(timezone.utc).isoformat(),#date en format iso
        "tool": nomtool,
        "args": args,
        "result": str(com)[:500] # on limite le resultat de la commande a 500 pour eviter qu'un enorme fichier casse les logs 
    }
    with open("logs/tool_calls.jsonl", "a")as f :
        f.write(json.dumps(entre)+ "\n")

#initialize the FastMCP server
mcp = MCPServer("aegis-access-lab")

@mcp.tool()
def fileRead(path:str)->str:
    """Cette fonction lit le contenue d'un fichier et le retourne """
    f = open(path) 
    log_app("fileRead",{"path":path},f)
    return f.read()

@mcp.tool()
def licommande(cmd:str)->str:
    """Éxécute une commande shell et retourne le résultat """
    com = subprocess.run(cmd, shell = True , capture_output=True , text=True) # l'utilisteur peut ici passer n'importe quel commande et on lira les resultat de cette commande en texte avec capture...
    log_app("licommande",{"cmd":cmd}, com)#retourn les logs des commandes
    return com.stdout + com.stderr

if __name__== "__main__":
    mcp.run()#démarre le serveur