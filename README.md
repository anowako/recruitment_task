# Opis narzędzia

Narzędzie służy do wyciągania danych z CV dostarczone w postaci obrazka. Dane, które otrzymuje użytkownik to umiejętności, które przedstawił kandydat wraz ze stopniem ich zaawansowania przedstawione za pomocą oceny w skali od 1 do 5 oraz wartości procentowej pobranej ze "skill bar".

# Uruchamianie

Aby uruchomić narzędzie należy zainstalować biblioteki z `requirements.txt`. A następnie wywołać komendę:
```bash
python main.py "./path"
```

gdzie w miejsce `"./path"` wstawiamy ścieżkę do pliku z CV, np. `"./examples/example1.png"`

# Struktura oraz wykorzystane biblioteki

Rozwiązanie ustrukturyzowane jest w sposób modułowy, aby w łatwy sposób można było modyfikować i dodawać funkcjonalności. Główny kod znajduje się w pliku `main.py`, a każda z funkcjonalności ustrukturyzwana jest w katalogach:

- `read_module` - odpowiedzialny jest za wczytywanie CV do dalszej analizy. Wykorzystywany do tego celu jest jeden z najpopularniejszych frameworków do analizy obrazu - **OpenCV**. Został wybrany, gdyż ma ogrom przydatnych funkcjonalności, które okazały się kluczowe podczas tworzenia całego systemu. Jest też łatwy do implementacji i przejrzysty, a skomplikowane działania można zapisać w kilku linijkach kodu.
- `ocr_module` - aby wydobyć informacje z dokumentu zapisanego za pomocą obrazu trzeba było dobrać odpowiednie narzędzie do OCR. W tym wypadku naturalnym wyborem był **EasyOCR**. Wygrywa z konkurencją lekkością swojego modelu oraz szybkością działania. Według wielu testów świetnie radzi sobie z wyciąganiem tekstu z dokumentów i także świetnie poradził sobie z CV.
- `skills_module` - opisuje całą logikę wyciągania informacji o umiejętnościach zapisanych w CV, a także wydobycia informacji o poziomie zaawansowana danej umiejętności ze "skill_bar". Do przetworzenia tekstu z OCR został użyty **NLTK**. Ponieważ nie było potrzeby stosowania tak dużych narzędzi jak chociażby Spacy. Modele NLTK cechują się lekkością oraz szybkością działania. Mają przy tym dużo funkcjonalności, które mogą być przydatne przy dalszym rozwijaniu narzędzia.
- `summary_module` - odpowiedzialny jest za podsumowanie profilu kandydata w oparciu o jego umiejętności. Wykorzystany został **model "LLaMA-2"** przetrenowany do odpowiedzi na pytania podczas zwykłej rozmowy. Świetnie radzi sobie z odpowiadaniem na pytanie, czy osoba z danymi umiejętnościami nadaje się na stanowisko np. Area Sales Manager. LLaMA-2 cechuje się szybkością i lekkością w porównaniu do swoich największych konkurentów, jak GPT-4. Jednakże co jest najważniejsze, jest to rozwiązanie open-source i można je dostosowywać do swoich potrzeb jak tylko chcemy.

# Logika rozwiązania

W `skills_module` dane z obrazka przechodzą następującą drogę:

- Z OCR wyciągana jest informacja gdzie znajduje się nagłówek opisujący umiejętności
- Informacje pod nagłówkiem traktowane są jako konkretne umiejętności
- Na obrazku szukamy prostokątów, które miałyby oznaczać "skill bar" - poszukiwania ograniczone są do części dokumentu po prawej stronie informacji oznaczających umiejętności
- Gdy po prawej stronie danej umiejętności wykryty został jeden prostokąt, oznacza to,e dana umiejętność jest na poziomie 100%, gdy wykryte zostały 2 prostokąty obok siebie, z szerokości obu pasków wyciągana jest informacja o procentowym posiomie danej umiejętności
- Wartości procentowe zamieniane są na wartości od 1 do 5

# Możliwości rozwoju

- Przedstwaione rozwiązanie zostało zaprojektowane w taki sposób, by w łatwy sposób można było dokonywać modyfikacji i dokładać nowych funkcjonalności np. moduł do wyciągania informacji o wykształceniu, czy poprzednim doświadczeniu. Takie dane mogą posłużyć jako dodatkowy input do modułu podsumowującego.
- Sam moduł podsumowujący może być trochę bardziej rozbudowany, bazując na różnych informacjach wejściowych mógłby je brać pod uwagę z inną wagą i generowałby jednoznaczną odpowiedź, czy np. zaprosić kandydata na rozmowę o pracę.
- Moduł do wyciągania informacji o umiejętnościach można bardziej dopracować, uwzględniając więcej przypadków wyglądu CV
