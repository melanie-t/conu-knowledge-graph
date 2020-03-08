curl http://localhost:2222/rest/annotate \
  -H "Accept: text/xml" \
  --data-urlencode "text=Brazilian state-run giant oil company Petrobras signed a three-year technology and research cooperation agreement with oil service provider Halliburton." \
  --data "confidence=0" \
  --data "support=0"

  read -p "Enter any key to exit."