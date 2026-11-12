from django.db.models import Sum
from django.utils import timezone
from .models import OrdemServico


def admin_dashboard_metrics(request):
    # Executa apenas se o utilizador estiver a aceder ao painel administrativo
    if request.path.startswith('/admin/'):
        hoje = timezone.now()
        os_mes = OrdemServico.objects.filter(data_abertura__month=hoje.month, data_abertura__year=hoje.year)

        faturamento_total = os_mes.filter(status='CONCLUIDO').aggregate(Sum('valor_orcamento'))[
                                'valor_orcamento__sum'] or 0
        gastos_total = os_mes.filter(status='CONCLUIDO').aggregate(Sum('custo_pecas'))['custo_pecas__sum'] or 0
        lucro_total = faturamento_total - gastos_total

        return {
            'faturamento_total': faturamento_total,
            'gastos_total': gastos_total,
            'lucro_total': lucro_total,
            'qtd_pendente': os_mes.filter(status='PENDENTE').count(),
            'qtd_andamento': os_mes.filter(status='ANDAMENTO').count(),
            'qtd_concluido': os_mes.filter(status='CONCLUIDO').count(),
            'qtd_cancelado': os_mes.filter(status='CANCELADO').count(),
        }
    return {}