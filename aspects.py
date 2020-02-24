varnish_aspect = {
    'request_rate': {
        'values': {
            'backend_unhealthy': {
                'min': '0',
                'type': 'DERIVE',
                'colour': 'FF55FF'
            },
            'cache_miss': {
                'min': '0',
                'draw': 'STACK',
                'type': 'DERIVE',
                'colour': 'FF0000'
            },
            'client_req': {
                'colour': '111111',
                'type': 'DERIVE',
                'min': '0'
            },
            's_pass': {
                'min': '0',
                'colour': '785d0d',
                'type': 'DERIVE'
            },
            'sess_conn': {
                'min': '0',
                'colour': '444444',
                'type': 'DERIVE',
                'graph': 'ON'
            },
            'cache_hit': {
                'min': '0',
                'draw': 'AREA',
                'colour': '00FF00',
                'type': 'DERIVE'
            },
            's_pipe': {
                'colour': '1d2bdf',
                'type': 'DERIVE',
                'min': '0'
            },
            'backend_conn': {
                'type': 'DERIVE',
                'colour': '995599',
                'min': '0'
            },
            'cache_hitpass': {
                'min': '0',
                'draw': 'STACK',
                'type': 'DERIVE',
                'colour': 'FFFF00',
                'info': 'Hitpass are cached passes: An entry in the cache instructing Varnish to pass. Typically achieved after a pass in vcl_fetch.'
            }
        },
        'order': 'cache_hit cache_hitpass cache_miss backend_conn backend_unhealthy client_req client_conn',
        'title': 'Request rates'
    },
    'vcl': {
        'values': {
            'n_backend': {
                'type': 'GAUGE'
            },
            'n_vcl_discard': {
                'type': 'DERIVE',
                'min': '0'
            },
            'n_vcl_avail': {
                'type': 'DERIVE',
                'min': '0'
            },
            'n_vcl': {
                'type': 'DERIVE',
                'min': '0'
            }
        },
        'title': 'VCL',
        'DEBUG': 'yes'
    },
    'uptime': {
        'vlabel': 'days',
        'scale': 'no',
        'title': 'Varnish uptime',
        'values': {
            'uptime': {
                'type': 'GAUGE',
                'cdef': 'uptime,86400,/'
            }
        }
    },
    'memory_usage': {
        'vlabel': 'bytes',
        'title': 'Memory usage',
        'args': '--base 1024',
        'values': {
            's0.g_bytes': {
                'type': 'GAUGE',
                'counter': 'g_bytes'
            },
            'Transient.g_bytes': {
                'type': 'GAUGE',
                'counter': 'g_bytes'
            },
            's0.c_bytes': {
                'type': 'GAUGE',
                'counter': 'c_bytes'
            },
            'Transient.c_bytes': {
                'type': 'GAUGE',
                'counter': 'c_bytes'
            },
            's0.g_space': {
                'type': 'GAUGE',
                'counter': 'g_space'
            },
            'Transient.g_space': {
                'type': 'GAUGE',
                'counter': 'g_space'
            }
        }
    },
    'session': {
        'values': {
            'sess_drop': {
                'min': '0',
                'type': 'DERIVE'
            },
            'sess_queued': {
                'min': '0',
                'type': 'DERIVE'
            },
            'sess_pipe_overflow': {
                'type': 'DERIVE',
                'min': '0'
            },
            'sess_readahead': {
                'type': 'DERIVE',
                'min': '0'
            },
            'sess_closed': {
                'type': 'DERIVE',
                'min': '0'
            },
            'sess_conn': {
                'type': 'DERIVE',
                'min': '0'
            },
            'sess_dropped': {
                'type': 'DERIVE',
                'min': '0'
            },
            'sess_fail': {
                'type': 'DERIVE',
                'min': '0'
            },
            'sess_pipeline': {
                'min': '0',
                'type': 'DERIVE'
            }
        },
        'DEBUG': 'yes',
        'title': 'Sessions'
    },
    'esi': {
        'DEBUG': 'yes',
        'title': 'ESI',
        'values': {
            'esi_errors': {
                'min': '0',
                'type': 'DERIVE'
            },
            'esi_warnings': {
                'type': 'DERIVE',
                'min': '0'
            },
            'esi_parse': {
                'type': 'DERIVE',
                'min': '0'
            }
        }
    },
    'lru': {
        'DEBUG': 'yes',
        'title': 'LRU activity',
        'values': {
            'n_lru_nuked': {
                'type': 'DERIVE',
                'min': '0'
            },
            'n_lru_moved': {
                'type': 'DERIVE',
                'min': '0'
            }
        }
    },
    'hit_rate': {
        'scale': 'no',
        'vlabel': '%',
        'title': 'Hit rates',
        'values': {
            'client_req': {
                'rpn': ['cache_hit', 'cache_miss', 'cache_hitpass', '+', '+'],
                'graph': 'off',
                'type': 'DERIVE',
                'min': '0'
            },
            'cache_miss': {
                'cdef': 'cache_miss,client_req,/,100,*',
                'draw': 'STACK',
                'min': '0',
                'type': 'DERIVE'
            },
            'cache_hitpass': {
                'cdef': 'cache_hitpass,client_req,/,100,*',
                'type': 'DERIVE',
                'min': '0',
                'draw': 'STACK'
            },
            'cache_hit': {
                'type': 'DERIVE',
                'min': '0',
                'draw': 'AREA',
                'cdef': 'cache_hit,client_req,/,100,*'
            }
        },
        'order': 'client_req cache_hit cache_miss cache_hitpass',
        'args': '-l 0 -u 100 --rigid'
    },
    'allocations': {
        'title': 'Memory allocation requests',
        'DEBUG': 'yes',
        'values': {
            'sma_nreq': {
                'min': '0',
                'type': 'DERIVE'
            },
            'sm_nreq': {
                'min': '0',
                'type': 'DERIVE'
            },
            'sms_nreq': {
                'type': 'DERIVE',
                'min': '0'
            }
        }
    },
    'bad': {
        'title': 'Misbehavior',
        'values': {
            'threads_failed': {
                'type': 'DERIVE'
            },
            'sess_drop': {
                'type': 'DERIVE'
            },
            'SMF_1': {
                'counter': 'c_fail',
                'family': 'SMF'
            },
            'backend_busy': {
                'type': 'DERIVE'
            },
            'SMA_1': {
                'counter': 'c_fail',
                'family': 'SMA'
            },
            'esi_warnings': {
                'type': 'DERIVE'
            },
            'sess_fail': {
                'type': 'DERIVE'
            },
            'threads_destroyed': {
                'type': 'DERIVE'
            },
            'losthdr': {
                'type': 'DERIVE'
            },
            'threads_limited': {
                'type': 'DERIVE'
            },
            'sess_pipe_overflow': {
                'type': 'DERIVE'
            },
            'thread_queue_len': {
                'type': 'GAUGE'
            },
            'esi_errors': {
                'type': 'DERIVE'
            },
            'fetch_failed': {
                'type': 'DERIVE'
            },
            'backend_unhealthy': {
                'type': 'DERIVE'
            }
        }
    },
    'threads': {
        'title': 'Thread status',
        'values': {
            'threads_failed': {
                'warning': ':1',
                'type': 'DERIVE',
                'min': '0'
            },
            'threads': {
                'warning': '1:',
                'type': 'GAUGE',
                'min': '0'
            },
            'threads_destroyed': {
                'type': 'DERIVE',
                'min': '0',
                'warning': ':1'
            },
            'threads_created': {
                'type': 'DERIVE',
                'min': '0'
            },
            'threads_limited': {
                'type': 'DERIVE',
                'min': '0'
            }
        }
    },
    'backend_traffic': {
        'values': {
            'backend_retry': {
                'min': '0',
                'type': 'DERIVE'
            },
            'backend_fail': {
                'min': '0',
                'type': 'DERIVE'
            },
            'backend_busy': {
                'min': '0',
                'type': 'DERIVE'
            },
            'backend_conn': {
                'type': 'DERIVE',
                'min': '0'
            },
            'backend_req': {
                'type': 'DERIVE',
                'min': '0'
            },
            # 'backend_toolate': {
            #     'min': '0',
            #     'type': 'DERIVE'
            # },
            'backend_reuse': {
                'type': 'DERIVE',
                'min': 0
            },
            'backend_unhealthy': {
                'warning': ':1',
                'type': 'DERIVE',
                'min': '0'
            },
            'backend_recycle': {
                'min': 0,
                'type': 'DERIVE'
            }
        },
        'title': 'Backend traffic'
    },
    'transfer_rates': {
        'vlabel': 'bit/s',
        'title': 'Transfer rates',
        'values': {
            's_resp_hdrbytes': {
                'min': '0',
                'label': 'Header traffic',
                'draw': 'STACK',
                'type': 'DERIVE',
                'info': 'HTTP Header traffic. TCP/IP overhead is not included.',
                'cdef': 's_resp_hdrbytes,8,*'
            },
            's_resp_bodybytes': {
                'draw': 'AREA',
                'min': '0',
                'type': 'DERIVE',
                'cdef': 's_resp_bodybytes,8,*',
                'label': 'Body traffic'
            }
        },
        'args': '-l 0',
        'order': 's_resp_bodybytes s_resp_hdrbytes'
    },
    'bans_lurker': {
        'title': 'Ban Lurker',
        'DEBUG': 'yes',
        'values': {
            'bans_lurker_tests_tested': {
                'type': 'DERIVE',
                'min': '0'
            },
            'bans_lurker_tested': {
                'type': 'DERIVE',
                'min': '0'
            },
            'bans_lurker_obj_killed': {
                'type': 'DERIVE',
                'min': '0'
            },
            'bans_lurker_contention': {
                'type': 'DERIVE',
                'min': '0'
            }
        }
    },
    'losthdr': {
        'values': {
            'losthdr': {
                'min': '0',
                'type': 'DERIVE'
            }
        },
        'title': 'HTTP Header overflows',
        'DEBUG': 'yes'
    },
    'session_herd': {
        'title': 'Session herd',
        'DEBUG': 'yes',
        'values': {
            'sess_herd': {
                'min': '0',
                'type': 'DERIVE'
            }
        }
    },
    'objects_per_objhead': {
        'title': 'Objects per objecthead',
        'DEBUG': 'yes',
        'values': {
            'obj_per_objhead': {
                'rpn': ['n_object', 'n_objecthead', '/'],
                'type': 'GAUGE',
                'label': 'Objects per object heads'
            }
        }
    },
    'hcb': {
        'values': {
            'hcb_lock': {
                'type': 'DERIVE',
                'min': '0'
            },
            'hcb_nolock': {
                'min': '0',
                'type': 'DERIVE'
            },
            'hcb_insert': {
                'min': '0',
                'type': 'DERIVE'
            }
        },
        'title': 'Critbit data',
        'DEBUG': 'yes'
    },
    'gzip': {
        'DEBUG': 'yes',
        'title': 'GZIP activity',
        'values': {
            'n_gunzip': {
                'min': '0',
                'type': 'DERIVE'
            },
            'n_gzip': {
                'min': '0',
                'type': 'DERIVE'
            }
        }
    },
    'expunge': {
        'title': 'Object expunging',
        'values': {
            'n_expired': {
                'min': '0',
                'type': 'DERIVE'
            },
            'n_lru_nuked': {
                'min': '0',
                'type': 'DERIVE'
            }
        },
        'order': 'n_expired n_lru_nuked'
    },
    'bans': {
        'values': {
            'bans_obj': {
                'type': 'GAUGE'
            },
            'bans_added': {
                'type': 'DERIVE',
                'min': '0'
            },
            'bans_deleted': {
                'type': 'DERIVE',
                'min': '0'
            },
            'bans_obj_killed': {
                'min': '0',
                'type': 'DERIVE'
            },
            'bans_req': {
                'type': 'GAUGE'
            },
            'bans_completed': {
                'type': 'GAUGE'
            },
            'bans_persisted_bytes': {
                'type': 'GAUGE'
            },
            'bans_dups': {
                'type': 'GAUGE'
            },
            'bans_tested': {
                'min': '0',
                'type': 'DERIVE'
            },
            'bans_persisted_fragmentation': {
                'type': 'GAUGE'
            },
            'bans': {
                'type': 'GAUGE'
            },
            'bans_tests_tested': {
                'min': '0',
                'type': 'DERIVE'
            }
        },
        'DEBUG': 'yes',
        'title': 'Bans'
    },
    'objects': {
        'title': 'Number of objects',
        'order': 'n_object n_objectcore n_vampireobject n_objecthead',
        'values': {
            'n_objectcore': {
                'type': 'GAUGE',
                'label': 'Number of object cores'
            },
            'n_object': {
                'type': 'GAUGE',
                'label': 'Number of objects'
            },
            'n_vampireobject': {
                'type': 'GAUGE',
                'label': 'Number of unresurrected objects'
            },
            'n_objecthead': {
                'type': 'GAUGE',
                'label': 'Number of object heads',
                'info': 'Each object head can have one or more object attached, typically based on the Vary: header'
            }
        }
    },
    'shm_writes': {
        'values': {
            'shm_writes': {
                'min': '0',
                'type': 'DERIVE'
            },
            'shm_records': {
                'min': '0',
                'type': 'DERIVE'
            }
        },
        'title': 'SHM writes and records',
        'DEBUG': 'yes'
    },
    'shm': {
        'values': {
            'shm_cont': {
                'type': 'DERIVE',
                'min': '0'
            },
            'shm_cycles': {
                'min': '0',
                'type': 'DERIVE'
            },
            'shm_flushes': {
                'min': '0',
                'type': 'DERIVE'
            }
        },
        'title': 'Shared memory activity',
        'DEBUG': 'yes'
    }
}