from flask import Flask, request
import json

# criação do servidor flask
app = Flask(__name__)

# curl -X POST -H "Content-Type: application/json" -d '{"url":"~/wpscan_output"}' http://localhost:5000/wordpress
@app.route('/wordpress', methods=['POST'])
def wordpress():
    wordpress_response = {}
    # NORMALIZA OS DADOS DIGITADO
    url_json = dict(request.get_json(force=True))
    # ABRINDO A SAIDA DO WPSCAN
    scan_response = open(url_json['url'],)
    # CONVERTENDO EM JSON
    scan_data = json.load(scan_response)

    # BUSCA AS INFORMACOES DE TECNOLOGIAS Q ESTAO SENDO USADAS E SUAS VERSOES
    wordpress_response = wp_web_server(scan_data['interesting_findings'][0]['interesting_entries'], wordpress_response)
    wordpress_response = get_infos('xml_rpc', scan_data['interesting_findings'][1]['url'], wordpress_response)
    wordpress_response = get_infos('readme', scan_data['interesting_findings'][2]['url'], wordpress_response)
    wordpress_response = get_infos('wp_cron', scan_data['interesting_findings'][3]['url'], wordpress_response)

    # VERSAO DO WORDPRESS
    if scan_data['version']['number']:
        wordpress_response.update({"wp_version":scan_data['version']['number']})

    # ISSUES MOSTRANDO A VERSAO
    if scan_data['version']['interesting_entries']:
        wordpress_response.update({"wp_version_issue":scan_data['version']['interesting_entries']})

    # TEMA USADO
    if scan_data['main_theme']['style_name']:
        theme = '%s %s' % (scan_data['main_theme']['style_name'], scan_data['main_theme']['version']['number'])
        wordpress_response.update({"theme":theme})

    # PLUGINS
    if scan_data['plugins']:
        plugins = []
        plugins_values = []
        for plugin in scan_data['plugins'].keys():
            plugins_values.append(plugin)
        for value in plugins_values:
            plugins.append('%s %s' % (value, scan_data['plugins'][value]['version']['number']))
            wordpress_response.update({"plugins":plugins})

    return wordpress_response

def wp_web_server(web_server_infos, wordpress_response):
    if web_server_infos:
        web_server = []
        for value in web_server_infos:
            web_server.append(value)
        if web_server[0]: wordpress_response.update({"web_server":web_server[0]})
        if web_server[1]: wordpress_response.update({"php_version":web_server[1]})
        return wordpress_response
    else:
        return False

def get_infos(key, infos, wordpress_response):
    if infos:
        wordpress_response.update({key:infos})
        return wordpress_response
    else:
        return False

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000',debug=True)
