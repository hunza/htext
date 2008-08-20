# -*- coding: utf-8 -*-
import re
from textutil_ja import kana

__all__ = ['romanize']

def romanize(value):
    value = kana.to_katakana(value)

    def step1(matcher):
        return MAP[matcher.group(1)]
    value = RE_KANA_TWO.sub(step1, value)
    value = RE_KANA_ONE.sub(step1, value)

    ## ッta -> tta
    def step2(matcher):
        char = matcher.group(1)
        return u'%s%s' % (char, char)
    value = RE_CONSONANTS.sub(step2, value)

    ## oー -> oo
    def step3(matcher):
        vowel = matcher.group(1)
        return u'%s%s' % (vowel, vowel)
    value = RE_VOWELS.sub(step3, value)

    return value

_MAP = u"""
  ア   a       イ   i       ウ   u       エ   e       オ   o
  ァ   xa      ィ   xi      ゥ   xu      ェ   xe      ォ   xo
  カ   ka      キ   ki      ク   ku      ケ   ke      コ   ko
  ガ   ga      ギ   gi      グ   gu      ゲ   ge      ゴ   go
  キャ kya                  キュ kyu                  キョ kyo
  サ   sa      シ   shi     ス   su      セ   se      ソ   so
  ザ   za      ジ   ji      ズ   zu      ゼ   ze      ゾ   zo
  シャ sha                  シュ shu                  ショ sho
  ジャ ja                   ジュ ju                   ジョ jo
  タ   ta      チ   chi     ツ   tsu     テ   te      ト   to
               ティ ti      トゥ tu
  ダ   da      ディ di      ドゥ du      デ   de      ド   do
               ヂ   dhi     ヅ   dhu
  チャ cha                  チュ chu     チェ che     チョ cho
  ヂャ dha                  ヂュ dhu     ヂェ dhe     ヂョ dho
  ナ   na      ニ   ni      ヌ   nu      ネ   ne      ノ   no
  ハ   ha      ヒ   hi      フ   fu      ヘ   he      ホ   ho
  ヒャ hya                  ヒュ hyu                  ヒョ hyo
  バ   ba      ビ   bi      ブ   bu      ベ   be      ボ   bo
  ビャ bya                  ビュ byu                  ビョ byo
  パ   pa      ピ   pi      プ   pu      ペ   pe      ポ   po
  ピャ pya                  ピュ pyu                  ピョ pyo
  ファ fa      フィ fi                   フェ fe      フォ fo
  マ   ma      ミ   mi      ム   mu      メ   me      モ   mo
  ヤ   ya                   ユ   yu      イェ ye      ヨ   yo
  ャ   xya                  ュ   xyu                  ョ   xyo
  ラ   ra      リ   ri      ル   ru      レ   re      ロ   ro
  ワ   wa      ヰ   wi                   ヱ   we      ヲ   wo
  ウァ wa      ウィ wi                   ウェ we      ウォ wo
  ヴァ va      ヴィ vi      ヴ   vu      ヴェ ve      ヴォ vo
  ン   n
""".split()

MAP = dict((k, v.upper()) for k, v in zip(_MAP[0::2], _MAP[1::2]))

RE_KANA_TWO = re.compile(u'(%s)' % u'|'.join(x for x in MAP.keys() if len(x) == 2))
RE_KANA_ONE = re.compile(u'(%s)' % u'|'.join(x for x in MAP.keys() if len(x) == 1))

RE_VOWELS = re.compile(u'([AIUEO])ー')

# note the absense of n and m
RE_CONSONANTS = re.compile(u"ッ([BCDFGHJKLPQRSTVWXYZ])")
