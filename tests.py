import unittest
import tempfile

import models

class MetadataTestCase(unittest.TestCase):
    def test_parse_metadata(self):
        text = '''Date: 2014-07-01
Visible: True
URL: hello-world
Title: Hello World'''

        meta = models.parse_metadata(text)

        self.assertEquals('2014-07-01', meta['date'])
        self.assertEquals(True, meta['visible'])
        self.assertEquals('hello-world', meta['url'])
        self.assertEquals('Hello World', meta['title'])
        self.assertNotIn('content', meta)

    def test_parse_content(self):
        text = ['Title: Hello World', 'Content:',
                'Mussum ipsum cacilds, vidis litro abertis.']

        content = models.parse_content(text)

        self.assertIn('Mussum', content)
        self.assertIn('abertis', content)
        self.assertNotIn('Hello World', content)

    def test_read_from_file(self):
        filename = tempfile.mktemp()

        with open(filename, 'w') as f:
            f.write('Title: Hello World\n')
            f.write('Content: \n')
            f.write('Mussum ipsum cacilds, vidis litro abertis.')

        meta = models.get_fileinfo(filename)
        content = models.get_filecontent(filename)

        self.assertEquals('Hello World', meta['title'])
        self.assertIn('Mussum', content)
        self.assertIn('abertis', content)
        self.assertNotIn('Hello World', content)

    def test_get_post_by_url(self):
        post = models.get_post_by_url('sample-post')

        self.assertEquals(post.date, '2014-07-01')
        self.assertEquals(post.title, 'Sample Post')
        self.assertEquals(post.url, 'sample-post')


if __name__ == '__main__':
    unittest.main()