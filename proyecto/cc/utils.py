from django.shortcuts import redirect

class IsNotAuthenticatedMixin:
    """
    Pregunta si ya está registrado
    """
    redirect_url = "/list/"
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect(self.redirect_url)
