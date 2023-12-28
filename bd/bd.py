import cx_Oracle
import mysql.connector
import configparser
import sqlite3
cx_Oracle.init_oracle_client(lib_dir=r"C:\conec\instantclient_21_10")

class conexao():
    @staticmethod
    def conectar():
        config = configparser.ConfigParser()
        config.read('config.ini')
        db = conexao = cx_Oracle.connect(config['DATABASE']['user'], config['DATABASE']['passwd'],
                                         config['DATABASE']['host'])

        return db

    @staticmethod
    def conectarmagento():
        config = configparser.ConfigParser()
        config.read('config.ini')
        db = conexao =  mysql.connector.connect(host=config['DATABASEMAGENTO']['host'],
                                                database=config['DATABASEMAGENTO']['db'],
                                                user=config['DATABASEMAGENTO']['user'],
                                                password='6sjT53w7RH"6')

        return db

    @staticmethod
    def conectarbot():
        #db = conexao =  sqlite3.connect(r'\\192.168.100.150\banco\bot_monitoramento.db')
        #db = conexao =  sqlite3.connect(r'../bd/bot_monitoramento.db')
        db = conexao =  sqlite3.connect(r'..\bd\bot_monitoramento.db')
        return db