# Production Tester (PyQt6)

Production Tester on modulaarinen, säikeistetty ja laajennettava testauskäyttöliittymä, joka on rakennettu PyQt6:n päälle.  
Sovellus on suunniteltu tuotantotestausympäristöihin, joissa tarvitaan:
[![CI](https://github.com/rumajukka-alt/Product_Tester/actions/workflows/ci.yml/badge.svg)](https://github.com/rumajukka-alt/Product_Tester/actions)


- selkeä, instrumenttimainen käyttöliittymä
- erillinen testilogiikka (TestRunner)
- CANCEL- ja STOP-keskeytykset
- taustasäikeessä ajettava mittaus (QThread)
- brändäys JSON-tiedostosta
- simuloitu mittauslaite kehityskäyttöön

---

## 📁 Projektirakenne
C:.
│   main.py
│   README.md
│   VERSION
│   __init__.py
│
├───Assets
│   │   branding.json
│   │   branding.py
│   │   __init__.py
│   │
│   └───__pycache__
│           branding.cpython-311.pyc
│           __init__.cpython-311.pyc
│
├───Code
│   │   spec_loader.py
│   │   test_runner.py
│   │   test_worker.py
│   │   __init__.py
│   │
│   ├───hardware
│   │       commercial_measurement_device.py
│   │       __init__.py
│   │
│   ├───interfaces
│   │   │   measurement_device_interface.py
│   │   │   measurement_interface.py
│   │   │   product_interface.py
│   │   │   __init__.py
│   │   │
│   │   └───__pycache__
│   │           measurement_device_interface.cpython-311.pyc
│   │           __init__.cpython-311.pyc
│   │
│   ├───simulator
│   │   │   config.py
│   │   │   measurement_circuit.py
│   │   │   noise_model.py
│   │   │   product_sample.py
│   │   │   simulated_measurement_device.py
│   │   │   simulator.py
│   │   │   temperature_model.py
│   │   │   __init__.py
│   │   │
│   │   └───__pycache__
│   │           config.cpython-311.pyc
│   │           measurement_circuit.cpython-311.pyc
│   │           noise_model.cpython-311.pyc
│   │           product_sample.cpython-311.pyc
│   │           simulated_measurement_device.cpython-311.pyc
│   │           temperature_model.cpython-311.pyc
│   │           __init__.cpython-311.pyc
│   │
│   └───__pycache__
│           spec_loader.cpython-311.pyc
│           test_runner.cpython-311.pyc
│           test_worker.cpython-311.pyc
│           __init__.cpython-311.pyc
│
├───Spec
│       limits.json
│       __init__.py
│
├───UI
│   │   emergency_stop_button.py
│   │   main_window.py
│   │   oscilloscope_widget.py
│   │   pass_fail_indicator.py
│   │   run_ui_test.py
│   │   start_button.py
│   │   style.qss
│   │
│   └───__pycache__
│           emergency_stop_button.cpython-311.pyc
│           main_window.cpython-311.pyc
│           oscilloscope_widget.cpython-311.pyc
│           pass_fail_indicator.cpython-311.pyc
│           run_ui_test.cpython-311.pyc
│           start_button.cpython-311.pyc
│
└───__pycache__
        main.cpython-311.pyc
        __init__.cpython-311.pyc


---

## 🚀 Käynnistys

Asenna riippuvuudet:

```bash
pip install -r requirements.txt

## 🚀 Sovellus
python main.py

🧩 Ominaisuudet
✔ Säikeistetty testiajo (QThread + Worker)
Testi suoritetaan erillisessä säikeessä, jolloin UI ei jäädy ja CANCEL/STOP toimivat välittömästi.
✔ CANCEL
- keskeyttää testin
- palauttaa FAIL
- palauttaa START-napin READY-tilaan
✔ STOP (Emergency Stop)
- pysäyttää kaiken välittömästi
- palauttaa FAIL
- palauttaa START-napin READY-tilaan
✔ Brändäys JSON-tiedostosta
Assets/branding.json sisältää:
- työkalun nimen
- version
- yrityksen nimen
- brändivärit
✔ Simuloitu mittauslaite
Kehitystilassa mittaus tehdään simulaattorilla:
- ProductSample
- SimulatedMeasurementDevice
- MeasurementCircuit
✔ Laajennettava arkkitehtuuri
Kaikki UI-komponentit ovat omissa moduuleissaan.

🛠 Kehittäminen
Muokkaa brändiä
Assets/branding.json

Muokkaa testilogiikkaa
Code/test_runner.py

Lisää UI-komponentteja
UI/

Hallitse tyylia
style.qss

📄 Lisenssi
© 2026 BigJ
Kaikki oikeudet pidätetään.

