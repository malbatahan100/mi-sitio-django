{
  "version": 2,
  "buildCommand": "bash build.sh",
  "builds": [
    {
      "src": "mi_sitio/wsgi.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "mi_sitio/wsgi.py"
    }
  ]
}
