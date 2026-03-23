"""Simple static file server — only needed to install the PWA on the phone.
Once installed, the app works fully offline."""
import http.server
import os

os.chdir(os.path.dirname(__file__) or '.')

handler = http.server.SimpleHTTPRequestHandler
handler.extensions_map.update({'.js': 'text/javascript', '.json': 'application/json'})

print("Odprite na telefonu: http://<vas-ip>:3000")
print("Nato: 'Dodaj na zacetni zaslon' / 'Add to Home Screen'")
print("Po namestitvi streznik ni vec potreben.\n")

with http.server.HTTPServer(('0.0.0.0', 3000), handler) as server:
    print("Streznik tece na http://localhost:3000")
    server.serve_forever()
