# FurkanAl Mimari

## Katmanlar
- Core: Orchestrator, AgentManager, Security
- Agents: 7 uzman ajan
- Memory: kısa/uzun süreli ve proje hafızasına genişletilebilir store
- Tools: Capability Registry
- API: FastAPI
- UI: sonraki aşamada Control Center

## Güvenlik
HIGH risk işlemler varsayılan olarak açık onay gerektirir.
Kaynak kodu kendi kendine değiştirme yoktur; ileride sandbox + approval pipeline eklenmelidir.

## Sonraki geliştirme
1. Gerçek LLM adapter
2. SQLite kalıcı memory
3. Web search adapter
4. Git/code sandbox
5. Capability permission engine
6. WebSocket canlı aktivite
7. Control Center
8. Scheduler/automation
9. Test ve evaluation pipeline
