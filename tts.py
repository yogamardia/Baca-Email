from subprocess import check_output

class TTS:
    def read_text(self, text):
        text = text
        check_output(['espeak', '-s', '130', '-v', 'mb-id1', text])
