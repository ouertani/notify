PIPENV      ?= pipenv
RUNNER      ?= $(PIPENV) run
CF          ?= cf
CF_SPACE_ID ?= f2c9cbdc-9449-4da9-8825-899e3142f783
GIT_REMOTE  ?= https://github.com/govau/notify

list-branches:
	git ls-remote --heads ${GIT_REMOTE} | egrep "/feat-.*" | $(RUNNER) python remove_feat_prefix.py

list-apps:
	$(CF) curl "/v2/spaces/${CF_SPACE_ID}/apps" | jq -r ".resources[].entity.name"

list-services:
	$(CF) curl "/v2/spaces/${CF_SPACE_ID}/service_instances" | jq -r ".resources[].entity.name"

get-ups-id-%:
	$(CF) curl "/v2/user_provided_service_instances?q=name:$*" | jq ".resources[].metadata.guid"

get-ups-bindings-%:
	$(CF) curl "/v2/user_provided_service_instances/$*/service_bindings" | jq ".resources[].entity.app_guid"

get-app-name-%:
	$(CF) curl "/v2/apps/$*" | jq ".entity.name"

get-ups-apps-%:
	$(MAKE) -s get-ups-id-$* | \
		xargs printf -- 'get-ups-bindings-%s\n' | xargs $(MAKE) -s | \
		xargs printf -- 'get-app-name-%s\n' | xargs $(MAKE) -s

restage-ups-apps-%:
	$(MAKE) -s get-ups-apps-$* | xargs printf -- 'restage-app-%s\n' | xargs $(MAKE)

restage-app-%:
	$(CF) restage $*

undeploy-feature-branches:
	$(RUNNER) python undeploy_closed_branches.py

undeploy-%:
	-$(CF) unbind-service notify-api-f-$* notify-psql-f-$*
	-$(CF) unbind-service notify-celery-f-$* notify-psql-f-$*
	-$(CF) delete notify-f-$* -f
	-$(CF) delete notify-api-f-$* -f
	-$(CF) delete notify-celery-f-$* -f
	-$(CF) delete-service notify-psql-f-$* -f

.PHONY: list-branches list-apps list-services list-deployed-features prune
