
# FacturaRetencionApp

Una aplicación sencilla desarrollada en Python con [Kivy](https://kivy.org/) para ayudar a los entregadores a calcular la retención de una factura.

## 📲 Cálculo aplicado

- IVA = 16% de la base imponible
- Base imponible = total / 1.16
- Retención = 75% del IVA

## 🧰 Requisitos

- Python 3.8+
- Kivy
- Opcional: Buildozer para compilar APK en Android

## 🚀 Ejecutar la app

```bash
python main.py
```

## 📦 Compilar APK (opcional con Buildozer)

```bash
buildozer init
buildozer -v android debug
```
