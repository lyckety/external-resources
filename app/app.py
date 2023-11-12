"""
Module implements REST API
"""

from flask import Flask, request, Response, jsonify

from config import Config

import mikrotik
import bgp
import resolver


class App(object):
    """
    App web applicattion
    """
    def __init__(self, cfg: Config) -> None:
        self.__web: Flask = Flask(__name__)
        self.__cfg: Config = cfg

    def __register_handler(self) -> None:
        @self.__web.route('/api/v1/bgp/as/get-info')
        def get_info():
            return bgp.get_info(request.args.get('asn'))

        @self.__web.route('/api/v1/bgp/as/announces')
        def get_announces_as():
            return bgp.get_ip_prefix_announces(
                request.args.get('asn'),
                ip_type=request.args.get('ip_type')
            )

        @self.__web.route('/api/v1/bgp/as/get-full-info')
        def get_full_info_as():
            return bgp.get_full_info(request.args.get('asn'))

        @self.__web.route('/api/v1/bgp/as/get-announces-mikrotik-list')
        def get_announces_as_mikrotik_list():
            script = mikrotik.ip_prefixes_to_address_list(
                bgp.get_ip_prefix_announces(
                    request.args.get('asn'),
                    ip_type=request.args.get('ip_type'),
                ),
                request.args.get('list_name'),
                request.args.get('comment')
            )

            return Response(script, mimetype='text/plain')

        @self.__web.route('/api/v1/resolver/nslookup')
        def get_ips_from_domain_names():
            return jsonify(
                ips = resolver.resolve_ips(
                    *request.args.getlist('domain_name')
                )
            )

        @self.__web.route('/api/v1/resolver/nslookup-as-mikrotik-list')
        def get_ips_from_domain_names_as_mikrotik_list():
            script = mikrotik.ips_for_domain_to_address_list(
                resolver.resolve_ips(
                    *request.args.getlist('domain_name'),
                ),
                request.args.get('list_name'),
                request.args.get('comment_prefix')
            )

            return Response(script, mimetype='text/plain')

    def run(self) -> None:
        """
        Run web application
        """
        self.__register_handler()

        self.__web.run(
            debug=self.__cfg.is_debug_flask,
            host=self.__cfg.http_bind_address,
            port=self.__cfg.http_bind_port,
        )
