# -*- coding:utf-8 -*-

{
    'name': 'iBone CodeBar Etiquetador Lote',
    'version': '0.1.2',
    'depends': [
        'product'
        ],
    'author': 'Corpotek',
    'category': 'Inventario',
    'description': 'Generar código de barras para el ingreso de lotes',
    'website': 'https://corpotek.com/',
    'summary': 'Crear y gestionar el ingreso de artículos mediante determinadas propiedades, obteniendo un código de barras desde las propiedades establecidas',
    'data': [
        'security/seguridad.xml',
        'security/ir.model.access.csv',
        'data/secuencia.xml',
        'views/menu.xml',
        'views/ibonelotecodebar_view.xml',
        'views/ibone_lcb_busqueda_view.xml',
        'report/formatoRerportes.xml',
        'report/reporte_lotecodebar.xml',
    ]
}