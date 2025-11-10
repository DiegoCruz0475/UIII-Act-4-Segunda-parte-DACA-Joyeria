# UIII_joyeria_0475/app_joyeria/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Proveedor, Venta

def inicio_joyeria(request):
    return render(request, 'inicio.html')

# ==========================================
# VISTAS PARA PRODUCTO
# ==========================================
def agregar_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        material = request.POST.get('material')
        precio = request.POST.get('precio')
        tipo = request.POST.get('tipo')
        stock = request.POST.get('stock')
        id_proveedor = request.POST.get('id_proveedor')

        proveedor = get_object_or_404(Proveedor, pk=id_proveedor)

        producto = Producto(
            nombre=nombre,
            material=material,
            precio=precio,
            tipo=tipo,
            stock=stock,
            id_proveedor=proveedor
        )
        producto.save()
        return redirect('ver_productos')
    proveedores = Proveedor.objects.all()
    return render(request, 'producto/agregar_producto.html', {'proveedores': proveedores})

def ver_productos(request):
    productos = Producto.objects.all()
    return render(request, 'producto/ver_productos.html', {'productos': productos})

def actualizar_producto(request, id_producto):
    producto = get_object_or_404(Producto, pk=id_producto)
    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre')
        producto.material = request.POST.get('material')
        producto.precio = request.POST.get('precio')
        producto.tipo = request.POST.get('tipo')
        producto.stock = request.POST.get('stock')
        id_proveedor = request.POST.get('id_proveedor')
        producto.id_proveedor = get_object_or_404(Proveedor, pk=id_proveedor)
        producto.save()
        return redirect('ver_productos')
    proveedores = Proveedor.objects.all()
    return render(request, 'producto/actualizar_producto.html', {'producto': producto, 'proveedores': proveedores})

def borrar_producto(request, id_producto):
    producto = get_object_or_404(Producto, pk=id_producto)
    if request.method == 'POST':
        producto.delete()
        return redirect('ver_productos')
    return render(request, 'producto/borrar_producto.html', {'producto': producto})

# ==========================================
# VISTAS PARA PROVEEDOR
# ==========================================
def agregar_proveedor(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        tipo_suministro = request.POST.get('tipo_suministro')

        proveedor = Proveedor(
            nombre=nombre,
            apellido=apellido,
            direccion=direccion,
            telefono=telefono,
            correo=correo,
            tipo_suministro=tipo_suministro
        )
        proveedor.save()
        return redirect('ver_proveedores')
    return render(request, 'proveedor/agregar_proveedor.html')

def ver_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedor/ver_proveedores.html', {'proveedores': proveedores})

def actualizar_proveedor(request, id_proveedor):
    proveedor = get_object_or_404(Proveedor, pk=id_proveedor)
    if request.method == 'POST':
        proveedor.nombre = request.POST.get('nombre')
        proveedor.apellido = request.POST.get('apellido')
        proveedor.direccion = request.POST.get('direccion')
        proveedor.telefono = request.POST.get('telefono')
        proveedor.correo = request.POST.get('correo')
        proveedor.tipo_suministro = request.POST.get('tipo_suministro')
        proveedor.save()
        return redirect('ver_proveedores')
    return render(request, 'proveedor/actualizar_proveedor.html', {'proveedor': proveedor})

def borrar_proveedor(request, id_proveedor):
    proveedor = get_object_or_404(Proveedor, pk=id_proveedor)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('ver_proveedores')
    return render(request, 'proveedor/borrar_proveedor.html', {'proveedor': proveedor})

# Vistas para Venta (PENDIENTE)
def agregar_venta(request):
    pass
def ver_ventas(request):
    pass
def actualizar_venta(request, id_venta):
    pass
def borrar_venta(request, id_venta):
    pass