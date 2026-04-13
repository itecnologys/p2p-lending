// ═══════════════════════════════════════════════════════════
// NEXUS Platform — Mock Data
// Todos os dados de demonstração da plataforma
// ═══════════════════════════════════════════════════════════

const NEXUS = {

  // ── APLICANTE LOGADO (mock) ──────────────────────────────
  applicant: {
    id: "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    name: "João Carlos Silva",
    email: "joao.silva@email.com",
    cpf: "***.***.***-45",
    role: "applicant",
    kyc_level: 2,
    nexus_funding_score: 820,
    pix_key: "joao.silva@email.com",
    stats: {
      total_invested: 28500.00,
      total_return_ytd: 4732.50,
      net_return_ytd: 3954.80,
      active_investments: 4,
      monthly_rate_avg: 0.042,
      next_pix_date: "2026-05-01",
      next_pix_amount: 1187.50
    }
  },

  // ── USUÁRIO LOGADO (mock) ─────────────────────────────────
  user: {
    id: "u9w8v7u6-t5s4-3210-rqpo-nm9876543210",
    name: "Maria Fernanda Costa",
    email: "maria.costa@email.com",
    cpf: "***.***.***-12",
    role: "user",
    kyc_level: 2,
    nexus_score: 720,
    card: {
      masked_pan: "**** **** **** 4521",
      brand: "visa",
      status: "active",
      available_balance: 160.00,
      total_limit: 280.00,
      expiry: "12/28"
    },
    stats: {
      active_credits: 1,
      next_installment_date: "2026-05-05",
      next_installment_amount: 67.80,
      total_paid_installments: 3,
      total_remaining_installments: 3,
      days_to_next: 24
    }
  },

  // ── PORTFÓLIOS ───────────────────────────────────────────
  portfolios: [
    { id:"p001", name:"Portfólio Alfa", risk:"A", rate_min:0.030, rate_max:0.038,
      min_investment:500, capacity:85000, total_allocated:415000,
      active_contracts:312, default_rate:0.018, status:"open",
      description:"Portfólio de baixo risco com contratos de perfil premium (score ≥ 850)" },
    { id:"p002", name:"Portfólio Beta", risk:"B", rate_min:0.039, rate_max:0.045,
      min_investment:500, capacity:230000, total_allocated:770000,
      active_contracts:891, default_rate:0.031, status:"open",
      description:"Portfólio equilibrado — maior retorno com risco controlado (score ≥ 700)" },
    { id:"p003", name:"Portfólio Gama", risk:"C", rate_min:0.046, rate_max:0.050,
      min_investment:500, capacity:410000, total_allocated:590000,
      active_contracts:1204, default_rate:0.058, status:"open",
      description:"Portfólio de alto retorno com diversificação ampla (score ≥ 550)" },
    { id:"p004", name:"Portfólio Delta", risk:"A", rate_min:0.031, rate_max:0.036,
      min_investment:500, capacity:0, total_allocated:500000,
      active_contracts:428, default_rate:0.012, status:"closed",
      description:"Portfólio fechado — sem capacidade disponível no momento" },
    { id:"p005", name:"Portfólio Epsilon", risk:"B", rate_min:0.040, rate_max:0.044,
      min_investment:500, capacity:150000, total_allocated:350000,
      active_contracts:567, default_rate:0.027, status:"open",
      description:"Portfólio B de consumo — focado em verticais essenciais" },
  ],

  // ── APORTES DO APLICANTE ──────────────────────────────────
  investments: [
    { id:"inv001", portfolio:"Portfólio Beta",  risk:"B", amount:8000,  rate:0.042, term:12, start:"2025-07-01", maturity:"2026-07-01", status:"active", return_accum:2822.40, next_pix:387.00, macro_hash_l2:"a3f8c1d9e4b27053f1c8a97e621bb4d0" },
    { id:"inv002", portfolio:"Portfólio Alfa",  risk:"A", amount:5000,  rate:0.035, term:6,  start:"2025-11-01", maturity:"2026-05-01", status:"active", return_accum:628.75,  next_pix:198.75, macro_hash_l2:"b4g9d2e0f5c38164g2d9b08f732cc5e1" },
    { id:"inv003", portfolio:"Portfólio Gama",  risk:"C", amount:10000, rate:0.048, term:12, start:"2025-09-01", maturity:"2026-09-01", status:"active", return_accum:3312.00, next_pix:504.00, macro_hash_l2:"c5h0e3f1g6d49275h3e0c19g843dd6f2" },
    { id:"inv004", portfolio:"Portfólio Epsilon",risk:"B", amount:5500, rate:0.041, term:3,  start:"2026-02-01", maturity:"2026-05-01", status:"active", return_accum:453.95,  next_pix:97.75,  macro_hash_l2:"d6i1f4g2h7e50386i4f1d20h954ee7g3" },
  ],

  // ── SOLICITAÇÕES DE CRÉDITO ───────────────────────────────
  credits: [
    { id:"crd001", amount:280, blocks:7, vertical:"V049 Academia / crossfit",
      installments:6, rate:0.041, status:"disbursed",
      created:"2026-02-10", disbursed:"2026-02-10",
      macro_hash_l4:"e7j2g5h3i8f61497j5g2e31i065ff8h4",
      installments_paid:3, installments_total:6, installment_value:50.52 },
    { id:"crd002", amount:120, blocks:3, vertical:"V007 Delivery",
      installments:3, rate:0.038, status:"queued",
      created:"2026-04-11", queue_position:4, macro_hash_l4:null },
  ],

  // ── TRANSAÇÕES DO CARTÃO ──────────────────────────────────
  transactions: [
    { id:"t001", merchant:"Gympass",        vertical:"V049 Academia",    amount:89.90,  date:"2026-04-10", status:"settled", type:"purchase" },
    { id:"t002", merchant:"iFood",          vertical:"V007 Delivery",    amount:42.50,  date:"2026-04-09", status:"settled", type:"purchase" },
    { id:"t003", merchant:"Drogasil",       vertical:"V048 Farmácia",    amount:67.30,  date:"2026-04-08", status:"settled", type:"purchase" },
    { id:"t004", merchant:"Uber",           vertical:"V039 App Corrida", amount:24.70,  date:"2026-04-07", status:"settled", type:"purchase" },
    { id:"t005", merchant:"Supermercado",   vertical:"V001 Supermercado",amount:156.40, date:"2026-04-06", status:"settled", type:"purchase" },
    { id:"t006", merchant:"Netflix",        vertical:"V086 Streaming",   amount:39.90,  date:"2026-04-05", status:"settled", type:"purchase" },
    { id:"t007", merchant:"CRÉDITO NEXUS",  vertical:"Crédito",          amount:280.00, date:"2026-02-10", status:"settled", type:"credit_block", macro_hash:"e7j2g5h3i8f61497j5g2e31i065ff8h4" },
  ],

  // ── MACRO HASH LEDGER ─────────────────────────────────────
  ledger: [
    { level:1, label:"Platform State",  hash:"a3f8c1d9e4b27053f1c8a97e621bb4d03e5a1f82c7d94b06e3f2a8c5b91d740e", parent:null,     entity:"platform",  date:"2026-04-11" },
    { level:2, label:"Investor Block",  hash:"b4g9d2e0f5c38164g2d9b08f732cc5e1d6b2g93h8e05c19g954de851f",         parent:"a3f8...0e", entity:"inv001",    date:"2026-04-11" },
    { level:3, label:"Portfolio Block", hash:"c5h0e3f1g6d49275h3e0c19g843dd6f2e7c3h04i9f16d20h065ef962g",         parent:"b4g9...1f", entity:"p002",      date:"2026-04-11" },
    { level:4, label:"Contract Block",  hash:"d6i1f4g2h7e50386i4f1d20h954ee7g3f8d4i15j0g27e31i176fg073h",         parent:"c5h0...2g", entity:"crd001",    date:"2026-02-10" },
    { level:5, label:"Block State",     hash:"e7j2g5h3i8f61497j5g2e31i065ff8h4g9e5j26k1h38f42j287gh184i",         parent:"d6i1...3h", entity:"blk001",    date:"2026-02-10" },
  ],

  // ── NEXUS SCORE COMPONENTS ────────────────────────────────
  score_detail: {
    total: 720,
    components: [
      { label:"Histórico de Pagamentos",    weight:35, raw:68, contribution:238, color:"#1640D6" },
      { label:"Comportamento de Consumo",   weight:25, raw:71, contribution:177, color:"#059669" },
      { label:"Dados Financeiros Alternat.",weight:20, raw:74, contribution:148, color:"#D97706" },
      { label:"Cadastro e Relacionamento",  weight:12, raw:82, contribution:98,  color:"#0ea5e9" },
      { label:"Bureau Externo (Opcional)",  weight:8,  raw:74, contribution:59,  color:"#8B5CF6" },
    ],
    history: [
      { month:"Out/25", score:650 }, { month:"Nov/25", score:665 },
      { month:"Dez/25", score:680 }, { month:"Jan/26", score:695 },
      { month:"Fev/26", score:705 }, { month:"Mar/26", score:712 },
      { month:"Abr/26", score:720 },
    ]
  },

  // ── VERTICAIS (resumo por bloco) ──────────────────────────
  verticals_summary: {
    total: 141,
    categories: [
      { name:"Alimentação",         count:18, icon:"🍽️", used:true  },
      { name:"Moradia e Casa",      count:14, icon:"🏠", used:false },
      { name:"Transporte",          count:12, icon:"🚗", used:true  },
      { name:"Saúde e Bem-estar",   count:14, icon:"❤️", used:true  },
      { name:"Educação",            count:10, icon:"📚", used:false },
      { name:"Vestuário e Moda",    count:8,  icon:"👗", used:false },
      { name:"Beleza",              count:9,  icon:"💆", used:false },
      { name:"Lazer",               count:12, icon:"🎮", used:true  },
      { name:"Tecnologia",          count:8,  icon:"📱", used:false },
      { name:"Pet",                 count:6,  icon:"🐾", used:false },
      { name:"Esporte e Fitness",   count:6,  icon:"🏋️", used:true  },
      { name:"Serviços do Lar",     count:8,  icon:"🔧", used:false },
      { name:"Serviços Financeiros",count:7,  icon:"💼", used:false },
      { name:"Presentes e Social",  count:5,  icon:"🎁", used:false },
      { name:"Sustentabilidade",    count:4,  icon:"🌱", used:false },
    ]
  },

  // ── HELPERS ───────────────────────────────────────────────
  fmt: {
    brl: v => new Intl.NumberFormat('pt-BR', {style:'currency',currency:'BRL'}).format(v),
    pct: v => (v*100).toFixed(2).replace('.',',') + '%',
    date: d => new Date(d).toLocaleDateString('pt-BR'),
    short_hash: h => h.substring(0,8)+'...'+h.substring(h.length-6),
    score_label: s => s>=850?'Premium':s>=700?'Aprovado':s>=550?'Monitorado':s>=400?'Restrito':'Bloqueado',
    score_color: s => s>=850?'#059669':s>=700?'#1640D6':s>=550?'#D97706':s>=400?'#F59E0B':'#DC2626',
    risk_color: r => r==='A'?'tag-a':r==='B'?'tag-b':'tag-c',
    status_badge: s => {
      const m = {active:'badge-green',queued:'badge-blue',disbursed:'badge-green',
                 pending_payment:'badge-gold',approved:'badge-green',rejected:'badge-red',matured:'badge-navy'};
      return m[s]||'badge-navy';
    }
  }
};

// Exportar para uso nos módulos
if(typeof module \!== 'undefined') module.exports = NEXUS;
