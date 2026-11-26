"""Regression fixtures for source locations and the display statement scanner."""

import unittest

import leansrc


class SourceBoundaries(unittest.TestCase):
    def check_marker(self, source, marker=':=', kind='theorem'):
        lines = source.split('\n')
        expected = len(lines), lines[-1].rindex(marker)
        self.assertEqual(leansrc.statement_boundary(lines, 1, len(lines), kind), expected)

    def test_raw_strings_ignore_embedded_quotes_and_proof_markers(self):
        self.check_marker('theorem t : r#"fake " := inside"# = "x" := by trivial')
        self.check_marker('theorem t : r##"fake "#\nwhere := still literal"## = "x" := by trivial')

    def test_where_inside_unicode_names_is_not_a_keyword(self):
        for identifier in ('whereé', 'éwhere', 'where\N{COMBINING ACUTE ACCENT}', 'Pkg.where'):
            with self.subTest(identifier=identifier):
                self.check_marker(f'theorem t : {identifier} := by trivial')
        self.check_marker('structure X where', 'where', 'structure')

    def test_nested_comments_and_astral_source_columns(self):
        self.check_marker('theorem t : True /- 🧮 := /- nested -/ -/ := by trivial')
        self.check_marker('/- outer\n/- inner := -/\n-/\ntheorem «x.y :=» : True := by trivial')

    def test_legacy_xref_fields_and_located_imports(self):
        text = 'public meta import A B -- note\nnamespace N\n@[simp]\ntheorem indéf₁ : True := by trivial\nend N\n'
        legacy = leansrc.parse(text)
        self.assertEqual(set(legacy), {'imports', 'cmds', 'namespaces', 'sections', 'opens', 'variables'})
        located = leansrc.parse(text, source_locations=True)
        self.assertEqual(located['import_sites'], [('A', 1), ('B', 1)])
        self.assertEqual(located['declaration_sites'], [
            {'name': 'N.indéf₁', 'kind': 'theorem', 'line': 4, 'endLine': 4},
        ])


if __name__ == '__main__':
    unittest.main()
