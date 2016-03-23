import bs4
import re

import kolala

from kolala.character.Effect import Effect
from kolala.character.Quest import Quest
from kolala.character.Stat import Stat
import kolala.Config as Config
import kolala.Globals as Globals
from kolala.pagetypes.KoLPage import KoLPage


class CharPane(KoLPage):

    url = Config.url + 'charpane.php'

    @staticmethod
    def claim(response):
        return response.url.startswith(CharPane.url)

    @staticmethod
    def parse_page(text, character=None):
        if character is None:
            character = kolala.player
        pwd = re.search('var pwdhash = "([a-f0-9]+)"', text)

        Globals.pwd = pwd.group(1)

        soup = bs4.BeautifulSoup(text, 'html.parser')
        if 'Hardcore' in soup.text:
            character.hardcore = True
        tag = soup.find('a', href='charsheet.php')
        tag = tag.find_next('a')
        tag = tag.b
        character.name = tag.text
        tag = tag.next_element
        tag = tag.next_element

        bits = list(tag.stripped_strings)
        character.level = bits[0].split()[1]
        character.char_cls = bits[1]
        tag = tag.table
        tag = tag.find_next('table')
        stats = tag.find_all('tr')
        for s in stats:
            if 'Muscle' in s.text:
                character.stats.muscle = Stat(s.b.text)
            if 'Moxie' in s.text:
                character.stats.moxie = Stat(s.b.text)
            if 'Mysticality' in s.text:
                character.stats.mysticality = Stat(s.b.text)
            if 'Tipsiness' in s.text:
                character.liver = int(s.b.text)
            if 'Inebriety' in s.text:
                character.liver = int(s.b.text)
            if 'Temulency' in s.text:
                character.liver = int(s.b.text)
            if 'Drunkenness' in s.text:
                character.liver = int(s.b.text)
            if 'Fury' in s.text:
                character.fury = int(s.b.text.split()[0])
                character.furynote = s.span['alt'].split('\n')[1]

        character.drunk = 'falling-down drunk' in tag.text

        tag = tag.find_next('img', title='Hit Points')
        character.hp = Stat(tag.text)
        tag = tag.find_next('img')
        character.mp = Stat(tag.text)
        tag = soup.find('img', title='Meat')
        character.meat = int(tag.text.replace(',', ''))

        tag = soup.find('img', title='Adventures Remaining')
        character.adv = int(tag.text)

        character.quests = {}
        nudges = soup.find('table', id='nudges')
        nudges = nudges.find_all('tr')

        for nudge in nudges:
            quest = Quest(nudge['rel'])
            st = nudge.div.find_all('s')
            for s in st:
                s.string = u'\u2611 ' + s.text
            tasks = nudge.div.text.replace('*', '\n')
            tasks = tasks.replace('\t', ' ')
            tasks = tasks.split('\n')
            quest.description = tasks[0]
            for sub in range(1, len(tasks)):
                task = tasks[sub]
                if u'\u2611' not in task:
                    task = u'\u2610 ' + task.strip()
                task = task.strip()
                quest.subtasks.append(task)
            character.quests[quest.name] = quest

        character.effects = []
        effects = tag.find_next(text=re.compile('Effects:'))
        if effects is not None:
            effects = effects.find_next('table')
            effects = effects.find_all('tr')
            for effect in effects:
                character.effects.append(Effect(effect.text))

    def auto_action(self):
        CharPane.parse_page(self.response.text)
        return None
