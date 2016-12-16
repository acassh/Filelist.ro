from couchpotato.core.helpers.encoding import tryUrlencode
from .main import Base
from couchpotato.core.media.movie.providers.base import MovieProvider


def autoload():
    return Filelist()


class Filelist(MovieProvider, Base):
    cat_ids = [
        ([25], ['3d']),
        ([19], ['720p', '1080p']),
        ([3], ['dvdr']),
        ([1], ['brrip', 'dvdrip', 'scr', 'r5', 'tc', 'ts', 'cam']),
    ]
    cat_backup_id = 1

    def buildUrl(self, title, media, quality):
        query = tryUrlencode({
            'search': '"%s" %s' % (title, media['info']['year']),
            'cat': self.getCatId(quality)[0],
        })
        return query	


config = [{
    'name': 'filelist',
    'groups': [
        {
            'tab': 'searcher',
            'list': 'torrent_providers',
            'name': 'Filelist',
            'description': 'See <a href="https://filelist.ro">Filelist</a>',
            'wizard': True,
            'icon': ('AAABAAEAEBAAAAEAGABoAwAAFgAAACgAAAAQAAAAIAAAAAEAGAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAClhCylhCylhCylh'
                     'CylhCylhCylhCylhCylhCylhCylhCylhCylhCylhCylhCylhCylhCwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLS'
                     'wvLSwvLSwvLSylhCylhCwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSylhCylhCwvLSwvLSwvLSw'
                     'vLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSylhCylhCwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwv'
                     'LSwvLSwvLSylhCylhCwvLSwvLSwvLSzVoh8vLSwvLSwvLSwvLSzVoh/Voh/Voh/Voh8vLSwvLSylhCylhCwvLSwvLSyeeyPVo'
                     'h8vLSwvLSwvLSyeeyPVoh8vLSwvLSwvLSwvLSwvLSylhCylhCwvLSwvLSx8ZCbVoh/Voh/Voh9bTCl8ZCbVoh8vLSwvLSwvLS'
                     'wvLSwvLSylhCylhCwvLSwvLSxbTCnVoh8vLSwvLSwvLSx8ZCbVoh8vLSwvLSwvLSwvLSwvLSylhCylhCwvLSwvLSxbTCnVoh8'
                     'vLSwvLSwvLSxbTCnVoh8vLSwvLSwvLSwvLSwvLSylhCylhCwvLSwvLSxbTCnVoh/Voh/Voh/Voh9bTCnVoh8vLSwvLSwvLSwv'
                     'LSwvLSylhCylhCwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSylhCylhCwvLSwvLSwvLSwvLSwvL'
                     'SwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSylhCylhCwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLS'
                     'wvLSylhCylhCwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSwvLSylhCylhCylhCylhCylhCylhCylhCy'
                     'lhCylhCylhCylhCylhCylhCylhCylhCylhCylhCwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
                     'AAAAAAAAAAAAAAAAAAAAAAAAAAAA'),
            'options': [
                {
                    'name': 'enabled',
                    'type': 'enabler',
                    'default': False,
                },
                {
                    'name': 'username',
                    'default': '',
                },
                {
                    'name': 'password',
                    'default': '',
                    'type': 'password',
                },
                {
                    'name': 'seed_ratio',
                    'label': 'Seed ratio',
                    'type': 'float',
                    'default': 1,
                    'description': 'Will not be (re)moved until this seed ratio is met.',
                },
                {
                    'name': 'seed_time',
                    'label': 'Seed time',
                    'type': 'int',
                    'default': 48,
                    'description': 'Will not be (re)moved until this seed time (in hours) is met.',
                },
                {
                    'name': 'extra_score',
                    'advanced': True,
                    'label': 'Extra Score',
                    'type': 'int',
                    'default': 20,
                    'description': 'Starting score for each release found via this provider.',
                }
            ],
        },
    ],
}]
