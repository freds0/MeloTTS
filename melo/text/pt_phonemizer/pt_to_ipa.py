from .cleaner import portuguese_cleaners
from .gruut_wrapper import Gruut
import phonemizer

global_phonemizer = phonemizer.backend.EspeakBackend(
    language="ar",
    preserve_punctuation=True,
    with_stress=True,
    language_switch="remove-flags"
)    

def pt2ipa(text):
    #e = Gruut(language="pt-br", keep_puncs=True, keep_stress=False, use_espeak_phonemes=False)
    # text = spanish_cleaners(text)
    #phonemes = e.phonemize(text, separator="")

    phonemes = global_phonemizer.phonemize([text], strip=True, njobs=1)[0]
    return phonemes


if __name__ == '__main__':
  print(pt2ipa('A mancha móvel sobre a planície definiu-se no perfil de um pobre cavalo que passeava na verdura os seus olhos de velhice e fadiga, tristes e longos.'))